/* simple_canvas.js
Draws line that bounces around in the limits of the red box
*/
// canvas selector
const cnv = document.querySelector('#cnv')
const ctx = cnv.getContext('2d');

const width = ctx.canvas.clientWidth;
const height = ctx.canvas.clientHeight;

const center = {
  x: width/2, 
  y: height/2
}

const box = {
  x: 20,
  y: 20,
  w: width-40,
  h: height-40
}

const position = {
  x: center.x,
  y: center.y
}

function getAngle() {
  const deg = Math.floor(Math.random()*360)
  return [deg, Math.cos(deg), Math.sin(deg)]
}

let [deg, xstep, ystep] = getAngle()

const dampening = 0.8

function draw() {
    ctx.strokeStyle = 'red'
    ctx.beginPath();
    ctx.strokeRect(box.x, box.y, box.w, box.h)
    ctx.stroke()

    // draw line from center
    ctx.strokeStyle = 'black'
    ctx.beginPath();
    ctx.moveTo(position.x, position.y);
    if (box.x < position.x+xstep && position.x+xstep < box.x + box.w &&
        box.y < position.y+ystep && position.y+ystep < box.y + box.h) {
      position.x += xstep * 2
      position.y += ystep * 2
      ctx.lineTo(position.x, position.y)
      ctx.stroke()
    } else {
      [deg, xstep, ystep] = getAngle()
      position.x += (xstep * dampening)
      position.y += (ystep * dampening)    
    }

    window.requestAnimationFrame(draw)
}

draw()