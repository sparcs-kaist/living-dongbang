<template>
    <div>
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
            this.canvas.beginPath()
            this.canvas.moveTo(0, 0)
            this.canvas.rect(x, y, w, h)
            this.canvas.fillStyle = "lightgray"
            this.canvas.fill()
            this.canvas.strokeStyle = "black"
            this.canvas.stroke()
            this.canvas.font = "10px Georgia"
            this.canvas.textAlign = "center"
            this.canvas.textBaseline = "middle"
            this.canvas.fillStyle = "black"
            this.canvas.fillText(text, x+w/2, y+h/2)
        },
        rectDesk(x, y, w, h) {
            this.canvas.beginPath()
            this.canvas.moveTo(0, 0)
            this.canvas.rect(x, y, w, h)
            this.canvas.strokeStyle = "black"
            this.canvas.stroke()
        },
        arcDesk(x, y, w, h, a) {
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
            this.canvas.beginPath()
            this.canvas.moveTo(x, y)
            if(a === 1) {
                path.map(c => this.canvas.lineTo(x+c.x, y+c.y))
            } else if(a === 2) {
                path.map(c => this.canvas.lineTo(x+c.y, y+c.x))
            }
            this.canvas.closePath()
            this.canvas.strokeStyle = "black"
            this.canvas.stroke()
        }
    },
    mounted() {
        this.canvas = this.$refs.canvas.getContext('2d')
        this.rectArea(0, 0, 129, 342, "C사이트")
        this.rectArea(0, 492, 75, 20, "문")
        this.rectArea(480, 225, 20, 75, "문")

        var width = 77
        var height = 38

        var startX = 151
        var startY = 0
        this.rectDesk(startX, startY, width, height)
        this.rectDesk(startX+width, startY, width, height)
        this.rectDesk(startX+2*width, startY, width, height)

        startX = 151
        startY = 102
        this.rectDesk(startX, startY, width, height)
        this.rectDesk(startX, startY+height, width, height)
        this.rectDesk(startX+width, startY, width, height)
        this.rectDesk(startX+width, startY+height, width, height)

        startX = 404
        startY = 330
        this.rectDesk(startX, startY, height, width)
        this.rectDesk(startX+height, startY, height, width)
        this.rectDesk(startX, startY+width, height, width)
        this.rectDesk(startX+height, startY+width, height, width)

        startX = 242
        startY = 310
        this.arcDesk(startX, startY, 1, 1, 1)
        this.arcDesk(startX, startY, 1, -1, 1)
        this.arcDesk(startX, startY, -1, -1, 1)
        this.arcDesk(startX, startY, -1, 1, 1)

        startX = 397
        startY = 149
        this.arcDesk(startX, startY, 1, 1, 2)
        this.arcDesk(startX, startY, 1, -1, 2)
        this.arcDesk(startX, startY, -1, -1, 2)
        this.arcDesk(startX, startY, -1, 1, 2)
    }
}
</script>