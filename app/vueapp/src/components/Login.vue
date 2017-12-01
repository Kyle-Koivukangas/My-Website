<template>
<!-- Template for login modal. -->
    <div class="modal-mask" @click="close">
        <div class="modal-wrapper" > 
            <div class="modal-container" @click.stop>

                <div class="modal-header">
                    <slot name="header">
                        <h3 class="text-center">Login</h3>
                    </slot>
                </div>

                <div class="modal-body">
                    <slot name="body">
                        <form @submit.prevent="handlesubmit">
                            <label>
                                Username:
                                <input type="text" v-model="user.name"/>
                            </label>
                            <label>
                                Password:
                                <input type="password" v-model="user.password">
                            </label>
                            <button type="submit">Submit</button>
                        </form>
                    </slot>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

var instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  timeout: 1000,
  headers: {
    // "Access-Control-Allow-Origin": "*",
    "Accept": "application/json",
    "Content-Type": "application/json"
  }
});

export default {
  data() {
    return {
      user: {
        name: "",
        password: ""
      }
    };
  },
  methods: {
    handlesubmit() {
      axios
        .post("get_auth_token", {
          //   Authorization: 'token d2d5f9647d656bb4c34306a00c97f08ff7e9dde3',
          // Authorization: {'Access-Control-Allow-Origin': '*'},
          //   headers: {'Access-Control-Allow-Origin': '*'},
          //   withCredentials: true,
            auth: {
              username: this.user.name,
              password: this.user.password
            },
          username: this.user.name,
          password: this.user.password
        })
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    },
    close: function() {
      console.log("closing modal");
      this.$emit("close");
    }
  },
  mounted: function() {
    document.addEventListener("keydown", e => {
      if (this.show && e.keycode == 27) {
        this.close();
      }
    });
  }
};
</script>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css?family=Josefin+Slab|Ubuntu|Ubuntu+Condensed|Vollkorn|Lato");
$josefin: "Josefin Slab", serif;
$vollkorn: "Vollkorn", serif;
$ubuntu: "Ubuntu", sans-serif;
$ubuntucond: "Ubuntu Condensed", sans-serif;
$lato: "Lato", sans-serif;

h3 {
  font-family: $lato;
  margin-top: 0px;
  color: black !important;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 0;
  background-color: $white;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: $ubuntu;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 0px 0;
}

.modal-default-button {
  float: right;
}
</style>
