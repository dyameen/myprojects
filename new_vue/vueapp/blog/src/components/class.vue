<template>
    <div class="demo">
    <h1>In Class</h1>
        <p v-html="ht"></p>

        <h3>{{name}}</h3>
        <h3 v-once>{{name}}</h3>
        <h3>{{ok?"yes":"no"}}</h3>
        <button v-bind:disabled="disBtn" v-on:click = "updatetxt">Click Me!</button><br>
    </div>
</template>
<script>

export default {
        name : 'MyClass',
        components : {
        },
        props : {
            data : String,
            msg : String,
        },
        methods:{
            updatetxt(){
                this.name = "Karan",
                this.ok =! this.ok
            }
        },
        data(){
            return {
            show : true,
            name : "Yameen",
            ok : false,
            ht : "<h6>HTML Rendering</h6>",
            disBtn:false,
            //disBtn:true,
           }
        }
}

</script>

<style>
        .demo {
            height : 50%;
            width : 50%;
            background : yellow;
        }
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