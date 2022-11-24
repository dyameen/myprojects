<template>
    <div>
    <div class="div1">
        <h1>In Home</h1>
        <h2 v-if="show">{{data}}</h2>
        <h2 v-else>{{msg}}</h2>
            <button @click = "hello">Call Hello</button><br>
            <button v-on:click = "display">Toggle</button>
            <button @click="count++">
                Count is: {{ count }}
            </button>
    </div>
    <hr>
    <div class="div2">
        <MyUsers />
    </div>
    <hr>
    <div class="div3">
        <MyProd data="hi" msg="bye" />
    </div>
    <div class="div3">
        <MyClass />
    </div>
    </div>
</template>
<script>
import MyUsers from './Users.vue'
import MyProd from './Products.vue'
import MyClass from './class.vue'

export default {
        name : 'MyHome',
        components : {
            MyUsers,
            MyProd,
            MyClass,
        },
        props : {
            data : String,
            msg : String,
        },
        methods : {
            hello(){
                alert("hello console called.")
            },
            display(){
                this.show = !this.show
                //this.show = false
            }
        },
        data(){
            return {
            show : true,
            count : 0,
           }
        }
}

</script>

<style>

        .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            width: 100%;
            font-size: 1.0em;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            text-align: center;
        }
        .styled-table th {
            background-color: #009879;
            color: #ffffff;
            text-align: center;
        }
        .styled-table th,
        .styled-table td {
            padding: 12px 15px;

        }
        .styled-table  tr {
            border-bottom: 1px solid #dddddd;
        }

        .styled-table  tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }

        .styled-table  tr:last-of-type {
            border-bottom: 2px solid #009879;
        }
        .styled-table  tr.active-row {
            font-weight: bold;
            color: #009879;
        }

</style>