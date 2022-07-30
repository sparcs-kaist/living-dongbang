<template>
    <div id="quote-container">
        <div class="single-quote" v-for="(quote, index) in quotes" :key="index">
            <i>"{{ quote.text }}"</i> 
            <div class="speaker">- {{ quote.name }}({{ quote.nickname }})</div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            quotes: [{
                text: "Birth, Code, Die",
                name: "오승빈",
                nickname: "platypus"
            }, {
                text: "5호선! (술취한 권순호)",
                name: "권순호",
                nickname: "snowsuno"
            }, {
                text: "벗은 것도 이쁜 것 같아(???)",
                name: "박지호",
                nickname: "night"
            }, {
                text: "엥 상이 어디 있어? 저 RESTroom이요",
                name: "정상",
                nickname: "macintosh"
            }]
        }
    }
}
</script>

<style>
#quote-container {
    position: relative;
    margin-top: 20px;
    padding: 20px 25px;
    text-align: left;
    align-items: center;
    background-color: var(--light-gray);
    border-radius: 10px;
}
.single-quote {
    padding: 10px 0;
}
.speaker {
    margin-top: 15px;
    text-align: right;
    font-size: var(--font-small);
}
</style>