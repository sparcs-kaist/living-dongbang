<template>
    <div id="dongbang-map">
        <canvas id="canvas" ref="canvas" width="500" height="512" style="border: solid 1px black"></canvas>
    </div>
</template>

<script>
export default {
    data() {
        return {
            canvas: null,
        }
    },
    methods: {
        rectArea(x, y, w, h, text) {
            const { ctx } = this
            const area = new Path2D()
            ctx.beginPath()
            area.moveTo(0, 0)
            area.rect(x, y, w, h)
            area.closePath()
            ctx.fillStyle = "lightgray"
            ctx.fill(area)
            ctx.strokeStyle = "black"
            ctx.stroke(area)
            ctx.font = "10px Georgia"
            ctx.textAlign = "center"
            ctx.textBaseline = "middle"
            ctx.fillStyle = "black"
            ctx.fillText(text, x+w/2, y+h/2)
        },
        rectDesk(x, y, w, h, onClick) {
            const { canvas, ctx } = this
            const desk = new Path2D()
            ctx.beginPath()
            desk.moveTo(0, 0)
            desk.rect(x, y, w, h)
            desk.closePath()
            ctx.fillStyle = "white"
            ctx.fill(desk)
            ctx.strokeStyle = "black"
            ctx.stroke(desk)
            canvas.addEventListener('click', function (e) {
                if(ctx.isPointInPath(desk, e.offsetX, e.offsetY))
                    onClick()
            }),
            canvas.addEventListener('mousemove', function (e) {
                if(ctx.isPointInPath(desk, e.offsetX, e.offsetY))
                    ctx.fillStyle = "green"
                else 
                    ctx.fillStyle = "white"
                ctx.fill(desk)
                ctx.strokeStyle = "black"
                ctx.stroke(desk)
            })
        },
        arcDesk(x, y, w, h, a, onClick) {
            const { canvas, ctx } = this
            const desk = new Path2D()
            const path = [{
                x: 59*w, y: 0
            }, {
                x: 90*w, y: -45*h
            }, {
                x: 58*w, y: -68*h 
            }, {
                x: 38*w, y: -38*h
            }, {
                x: 0, y: -38*h
            }]
            ctx.beginPath()
            desk.moveTo(x, y)
            if(a === 1) {
                path.map(c => desk.lineTo(x+c.x, y+c.y))
            } else if(a === 2) {
                path.map(c => desk.lineTo(x+c.y, y+c.x))
            }
            desk.closePath()
            ctx.fillStyle = "white"
            ctx.fill(desk)
            ctx.strokeStyle = "black"
            ctx.stroke(desk)
            canvas.addEventListener('click', function (e) {
                if(ctx.isPointInPath(desk, e.offsetX, e.offsetY))
                    onClick()
            })
            canvas.addEventListener('mousemove', function (e) {
                if(ctx.isPointInPath(desk, e.offsetX, e.offsetY))
                    ctx.fillStyle = "green"
                else 
                    ctx.fillStyle = "white"
                ctx.fill(desk)
                ctx.strokeStyle = "black"
                ctx.stroke(desk)
            })
        }
    },
    mounted() {
        this.canvas = this.$refs.canvas
        this.ctx = this.$refs.canvas.getContext('2d')
        
        this.rectArea(0, 0, 129, 342, "C사이트")
        this.rectArea(0, 492, 75, 20, "문")
        this.rectArea(480, 225, 20, 75, "문")

        var width = 77
        var height = 38

        var startX = 151
        var startY = 0
        this.rectDesk(startX, startY, width, height, () => console.log("A1"))
        this.rectDesk(startX+width, startY, width, height, () => console.log("A2"))
        this.rectDesk(startX+2*width, startY, width, height, () => console.log("A3"))

        startX = 151
        startY = 102
        this.rectDesk(startX, startY, width, height, () => console.log("A4"))
        this.rectDesk(startX+width, startY, width, height, () => console.log("A5"))
        this.rectDesk(startX, startY+height, width, height, () => console.log("A6"))
        this.rectDesk(startX+width, startY+height, width, height, () => console.log("A7"))

        startX = 404
        startY = 330
        this.rectDesk(startX, startY, height, width, () => console.log("A8"))
        this.rectDesk(startX+height, startY, height, width, () => console.log("A9"))
        this.rectDesk(startX, startY+width, height, width, () => console.log("A10"))
        this.rectDesk(startX+height, startY+width, height, width, () => console.log("A11"))

        startX = 242
        startY = 310
        this.arcDesk(startX, startY, 1, 1, 1, () => console.log("B6"))
        this.arcDesk(startX, startY, 1, -1, 1, () => console.log("B8"))
        this.arcDesk(startX, startY, -1, -1, 1, () => console.log("B7"))
        this.arcDesk(startX, startY, -1, 1, 1, () => console.log("B5"))

        startX = 397
        startY = 149
        this.arcDesk(startX, startY, 1, 1, 2, () => console.log("B3"))
        this.arcDesk(startX, startY, 1, -1, 2, () => console.log("B4"))
        this.arcDesk(startX, startY, -1, -1, 2, () => console.log("B2"))
        this.arcDesk(startX, startY, -1, 1, 2, () => console.log("B1"))
    }
}
</script>

<style>
#dongbang-map {
    display: inline-block;
}
</style>