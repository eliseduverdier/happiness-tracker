
const canvas = document.getElementById("happiness-canvas");
const entryContextDiv = document.getElementById("entry-context");
const ctx = canvas.getContext("2d");

const leftPos = 25
const topPos = 50
const spaceBetweenLines = 40
const spaceBetweenDays = 50
const dateHeightPos = 25
const entriesObject = []
const daysNames = ['Su', 'M', 'Tu', 'W', 'Th', 'F', 'Sa']

showTimeOfDay()

let shiftingEmpties = 0
let x = 0

for (var i = 0; i < entries.length; i++) {
  // {'score': '🙂️', date:'dd/mm/yyyy', 'relative_days': 26, 'relative_days_since_last': 0, 'time': 'N', 'hour': 13, 'context': '...'}
  entriesObject[i] = new Path2D();

  // reduce space between long periods of time
  if (i > 0 && entries[i]['relative_days_since_last'] - entries[i - 1]['relative_days_since_last'] > 2) {
    // console.log(' >>> shift after '+entries[i-1]['date'])
    shiftingEmpties += (entries[i]['relative_days_since_last'] - entries[i - 1]['relative_days_since_last']) * spaceBetweenDays /*<- remove all space*/ - spaceBetweenDays * 2 /*<- but all a little*/
    ctx.font = "20px bold monospace";
    ctx.fillStyle = '#333';
    ctx.fillText('...', x + 50, dateHeightPos)
  }
  x = leftPos + (entries[i]['relative_days_since_last'] * spaceBetweenDays) + spaceBetweenLines - shiftingEmpties

  showSmiley(entries[i], i, x)

  if (i == 0 || entries[i]['date'] !== entries[i - 1]['date'])
    showDate(entries[i], x)
}


function showTimeOfDay() {
  ctx.fillStyle = "#333";
  ctx.font = "10px monospace";
  for (var i = 0; i <= 24; i++)
    ctx.fillText(i, leftPos, topPos + i * 20)
}

function showSmiley(entry, i, x) {
  ctx.font = "30px monospace";
  y = topPos + entry['hour'] * 20
  ctx.fillText(entry['score'], x, y)

  // save object to display hover text later
  if (entries[i]['context'] !== '') {
    entriesObject[i].arc(x + 15, y - 15, 20, 0, 2 * Math.PI);
    ctx.fillStyle = '#CCCC0000';
    ctx.fill(entriesObject[i]);

    ctx.fillStyle = '#cc5500';
    ctx.font = "20px monospace";
    ctx.fillText('*', x + 20, y - 20)

  }
}

function showDate(entry, x) {
  ctx.font = "10px monospace";
  ctx.fillStyle = '#555';
  d = new Date(entry['datejs'])
  if (d.getDay() === 0 || d.getDay() === 6) {
    line(x, dateHeightPos + 5, x + 40, dateHeightPos + 5)
    line(x, 555, x + 40, 555)
  }
  ctx.fillText(daysNames[d.getDay()] + entry['date'], x, dateHeightPos) // top
  ctx.fillText(daysNames[d.getDay()] + entry['date'], x, 550) // bottom
}


// https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/isPointInPath
canvas.addEventListener('mousemove', function (event) {
  for (var i = 0; i < entriesObject.length; i++) {
    if (ctx.isPointInPath(entriesObject[i], event.offsetX, event.offsetY)) {
      entryContextDiv.innerHTML = entries[i]['context'].replace(/\n/g, ' <br> ')
    }
  }
});

function line(x1, y1, x2, y2) {
  ctx.beginPath()
  ctx.moveTo(x1, y1)
  ctx.lineTo(x2, y2)
  ctx.stroke()
}
