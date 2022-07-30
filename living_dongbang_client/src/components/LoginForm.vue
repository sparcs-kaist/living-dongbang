<template>
    <div id="login-form">
        <img id="logo-img" v-bind:src="logoImg" width="200"/>
        <div class="form-input">
            <div class="label">아이디</div>
            <input v-model="userid" type="text" placeholder="User ID" />
        </div>
        <div class="form-input">
            <div class="label">비밀번호</div>
            <input v-model="password" type="password" placeholder="Password" />
        </div>
        <button id="login-button" @click="login">로그인</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            logoImg: require('../assets/SPARCS.png'),
            userid: '',
            password: ''
        }
    },
    methods: {
        onChangeUserID(e) {
            this.userid = e.target.value
        },
        onChangePassword(e) {
            this.userid = e.target.value
        },
        login() {
            console.log("Login with user " + this.userid)
        }
    }
}
</script>

<style>
#logo-img {
    margin: 20px;
}
.form-input {
    margin-bottom: 20px;
}
.label {
    color: var(--gray);
    text-align: left;
    padding: 5px;
    font-family: var(--font-kor);
    font-size: var(--font-middle);
}
input {
    width: calc(100% - 20px);
    height: 30px;
    padding: 5px 10px;
    border: solid 1px var(--gray);
    border-radius: 10px;
    font-family: var(--font-eng);
    font-size: var(--font-small);
}
#login-button {
    width: 100%;
    height: 40px;
    padding: 10px;
    margin: 20px 0;
    border: none;
    border-radius: 10px;
    color: var(--white);
    background-color: var(--orange);
    font-family: var(--font-kor);
    font-size: var(--font-large);
    font-weight: bold;
}
</style>