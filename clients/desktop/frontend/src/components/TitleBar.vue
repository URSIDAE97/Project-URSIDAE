<template>
  <div class="title-bar">
      <div class="window-name-container">
        <img 
            class="logo-icon"
            src="../assets/logos/transparent_white_no_title.png" 
            alt="logo" 
        />
        <p><slot></slot></p>
      </div>
      <div class="window-controls-container">
        <div
            id="minimize-button"
            class="minimize-button"
        >
            <img 
                class="minimize-icon"
                src="../assets/icons/minimize.png"
                alt="minimize"
            />
        </div>
        <div
            id="close-button"
            class="close-button"
        >
            <img 
                class="close-icon"
                src="../assets/icons/close.png"
                alt="close"
            />
        </div>
      </div>
    </div>
</template>

<script>
const { remote, ipcRenderer } = require('electron')

export default {
    mounted() {
        document.getElementById('minimize-button').addEventListener('click', () => {
            remote.getCurrentWindow().minimize()
        })
        document.getElementById('close-button').addEventListener('click', () => {
            remote.app.quit()
        })
    }
}
</script>

<style scoped>
.title-bar {
    width: 100%;
    height: 30px;
    background-color: rgb(20, 20, 20);
    -webkit-app-region: drag;
    margin: 0;
    display: flex;
    border-bottom: 1px solid rgb(0, 0, 0);
}

.window-name-container {
    display: flex;
    justify-content: left;
    align-items: center;
    flex-grow: 1;
    color: rgb(240, 240, 240)
}

.window-controls-container {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    flex-grow: 1;
}

.logo-icon {
    height: 65%;
    margin-left: 10px;
    margin-right: 10px;
}

.minimize-button {
    width: 40px;
    height: 100%;
    -webkit-app-region: no-drag;
    text-align: center;
}

.minimize-button:hover {
    background-color: rgb(40, 40, 40);
}

.minimize-icon {
    height: 85%;
}

.close-button {
    width: 40px;
    height: 100%;
    -webkit-app-region: no-drag;
    text-align: center;
}

.close-button:hover {
    background-color: rgb(100, 40, 40);
}

.close-icon {
    height: 100%;
}
</style>