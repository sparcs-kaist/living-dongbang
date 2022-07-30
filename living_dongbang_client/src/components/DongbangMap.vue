<template>
    <div id="dongbang-map">
        <canvas id="canvas" ref="canvas" width="500" height="512" style="border: solid 1px black"></canvas>
    </div>
</template>

<script>
import currentTime from '../helpers/time'
import useAuthStore from "../stores/auth.store";

export default {
    props: {
        reserveStatus: [String, String, String, String, String],
    },
    data() {
        return {
            canvas: null,
            timer: null,
            currentStatus: [],
            user: useAuthStore().username
        }
    },
    methods: {
        rectArea(x, y, w, h, text, color) {
            const { ctx } = this
            const area = new Path2D()
            ctx.beginPath()
            area.moveTo(0, 0)
            ctx.lineWidth = 1
            ctx.lineCap = "round"
            ctx.lineJoin = "round"
            area.rect(x, y, w, h)
            area.closePath()
            ctx.fillStyle = !color ? "#BBBBBB" : color
            ctx.fill(area)
            ctx.strokeStyle = "#333333"
            ctx.stroke(area)
            ctx.textAlign = "center"
            ctx.textBaseline = "middle"
            ctx.font = "bold 14px NanumSquare"
            ctx.fillStyle = !color ? "#333333" : color
            ctx.fillText(text, x+w/2, y+h/2)
        },
        rectDesk(x, y, w, h, onClick, label) {
            const { canvas, ctx } = this
            const desk = new Path2D()
            const reserved = this.currentStatus.find(s => s.seat === label)
            const username = reserved ? this.currentStatus.filter(s => s.seat === label).map(s => { return s.user })[0] : ""
            ctx.beginPath()
            desk.moveTo(0, 0)
            ctx.lineWidth = 1
            ctx.lineCap = "round"
            ctx.lineJoin = "round"
            desk.rect(x, y, w, h)
            desk.closePath()
            if(reserved)
                ctx.fillStyle = "red"
            else
                ctx.fillStyle = "white"
            ctx.fill(desk)
            ctx.strokeStyle = "#333333"
            ctx.stroke(desk)
            ctx.textAlign = "center"
            ctx.textBaseline = "middle"
            ctx.font = "bold 14px NanumSquare"
            ctx.fillStyle = "#333333"
            ctx.fillText(username, x+w/2, y+h/2)
            canvas.addEventListener('click', function (e) {
                if(ctx.isPointInPath(desk, e.offsetX, e.offsetY))
                    onClick()
            }),
            canvas.addEventListener('mousemove', function (e) {
                if(reserved) {
                    ctx.fillStyle = "red"
                } else if(ctx.isPointInPath(desk, e.offsetX, e.offsetY)) {
                    ctx.fillStyle = "#EC8F26"
                } else {
                    ctx.fillStyle = "white"
                }
                ctx.fill(desk)
                ctx.strokeStyle = "#333333"
                ctx.stroke(desk)
                ctx.fillStyle = "#333333"
                ctx.fillText(username, x+w/2, y+h/2)
            })
        },
        arcDesk(x, y, w, h, a, onClick, label) {
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
            const reserved = this.currentStatus.find(s => s.seat === label)
            const username = reserved ? this.currentStatus.filter(s => s.seat === label).map(s => { return s.user })[0] : ""
            ctx.beginPath()
            desk.moveTo(x, y)
            ctx.lineWidth = 1
            ctx.lineCap = "round"
            ctx.lineJoin = "round"
            if(a === 1) {
                path.map(c => desk.lineTo(x+c.x, y+c.y))
            } else if(a === 2) {
                path.map(c => desk.lineTo(x+c.y, y+c.x))
            }
            desk.closePath()
            if(reserved)
                ctx.fillStyle = "red"
            else
                ctx.fillStyle = "white"
            ctx.fill(desk)
            ctx.strokeStyle = "#333333"
            ctx.stroke(desk)
            ctx.textAlign = "center"
            ctx.textBaseline = "middle"
            ctx.font = "bold 14px NanumSquare"
            ctx.fillStyle = "#333333"
            if(a === 1) {
                ctx.fillText(username, x+35*w, y-20*h)
            } else if(a === 2) {
                ctx.fillText(username, x-35*h, y+20*w)
            }
            canvas.addEventListener('click', function (e) {
                if(ctx.isPointInPath(desk, e.offsetX, e.offsetY))
                    onClick()
            })
            canvas.addEventListener('mousemove', function (e) {
                if(reserved) {
                    ctx.fillStyle = "red"
                } else if(ctx.isPointInPath(desk, e.offsetX, e.offsetY)) {
                    ctx.fillStyle = "#EC8F26"
                } else {
                    ctx.fillStyle = "white"
                }
                ctx.fill(desk)
                ctx.strokeStyle = "#333333"
                ctx.stroke(desk)
                ctx.fillStyle = "#333333"
                if(a === 1) {
                    ctx.fillText(username, x+35*w, y-20*h)
                } else if(a === 2) {
                    ctx.fillText(username, x-35*h, y+20*w)
                }
            })
        },
        drawDongbang() {
            var width = 77
            var height = 38

            var startX = 151
            var startY = 0
            this.rectDesk(startX, startY, width, height, () => console.log("A1"), "A1")
            this.rectDesk(startX+width, startY, width, height, () => console.log("A2"), "A2")
            this.rectDesk(startX+2*width, startY, width, height, () => console.log("A3"), "A3")

            startX = 151
            startY = 102
            this.rectDesk(startX, startY, width, height, () => console.log("A4"), "A4")
            this.rectDesk(startX+width, startY, width, height, () => console.log("A5"), "A5")
            this.rectDesk(startX, startY+height, width, height, () => console.log("A6"), "A6")
            this.rectDesk(startX+width, startY+height, width, height, () => console.log("A7"), "A7")

            startX = 404
            startY = 330
            this.rectDesk(startX, startY, height, width, () => console.log("A8"), "A8")
            this.rectDesk(startX+height, startY, height, width, () => console.log("A9"), "A9")
            this.rectDesk(startX, startY+width, height, width, () => console.log("A10"), "A10")
            this.rectDesk(startX+height, startY+width, height, width, () => console.log("A11"), "A11")

            startX = 242
            startY = 310
            this.arcDesk(startX, startY, 1, 1, 1, () => console.log("B6"), "B6")
            this.arcDesk(startX, startY, 1, -1, 1, () => console.log("B8"), "B8")
            this.arcDesk(startX, startY, -1, -1, 1, () => console.log("B7"), "B7")
            this.arcDesk(startX, startY, -1, 1, 1, () => console.log("B5"), "B5")

            startX = 397
            startY = 149
            this.arcDesk(startX, startY, 1, 1, 2, () => console.log("B3"), "B3")
            this.arcDesk(startX, startY, 1, -1, 2, () => console.log("B4"), "B4")
            this.arcDesk(startX, startY, -1, -1, 2, () => console.log("B2"), "B2")
            this.arcDesk(startX, startY, -1, 1, 2, () => console.log("B1"), "B1")
        },
        findStatus(date, time) {
            this.currentStatus = this.reserveStatus.filter(s => date === s.date && s.startTime <= time && time <= s.endTime).map(s => { return { seat: s.seat, user: s.user }})
        },
        updateTime() {
            const today = new Date()
            const { date, time } = currentTime(today)
            this.findStatus(date, time)
        }
    },
    mounted() {
        this.canvas = this.$refs.canvas
        this.ctx = this.$refs.canvas.getContext('2d')
        
        this.rectArea(0, 0, 500, 512, "", "#FEF8EF")
        this.rectArea(0, 0, 129, 342, "C사이트")
        this.rectArea(0, 492, 75, 20, "문")
        this.rectArea(480, 225, 20, 75, "문")

        this.timer = setInterval(() => {
            this.updateTime()
            this.drawDongbang()
        }, 1000)
    },
    beforeUnmount() {
        clearInterval(this.timer)
    }
}
</script>

<style>
#dongbang-map {
    display: inline-block;
    font-family: var(--font-kor);
    padding: 30px 0;
}
</style>