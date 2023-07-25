<template>
    <div class="login-container">
      <button class="login-button" @click="loginWithGoogle">Googleログイン</button>
    </div>
  </template>
  
  
<script>
export default {
    data: () => ({
        isLogin: false,
    }),
    methods: {
        loginWithGoogle() {
            // console.log(this.isLogin)
            const client_id = "178463503249-0e4ibfanbtmd30esgjamvvhe2a1nsvv7.apps.googleusercontent.com"; 
            const redirect_uri = "https://gmc.cps.akita-pu.ac.jp/"; 
            const auth_url = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${client_id}&response_type=token&scope=openid%20email%20profile&redirect_uri=${redirect_uri}`;
            window.location.href = auth_url;
        }
    },
    mounted() {
        // URLパラメーターからアクセストークンを取得
        // console.log(this.isLogin)
        const token = new URLSearchParams(window.location.hash.substr(1)).get("access_token");
        if (token) {
            this.$router.push('/home');
            this.isLogin = true;
            // console.log(this.isLogin)
        }
    },
};
</script>

<style>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-button {
  padding: 12px 24px;
  font-size: 16px;
  font-weight: bold;
  background-color: #4285f4;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.login-button:hover {
  background-color: #2d74da;
}

.login-button:focus {
  outline: none;
}

</style>
  