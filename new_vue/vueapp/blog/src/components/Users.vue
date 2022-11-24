<template>
    <div class="div2">
    <h1>In User</h1>
    <table class="styled-table" border="1">
        <tr>
            <th>Id</th>
            <th>User</th>
            <th>Email</th>
        </tr>
        <tr v-for="i in users" :key="i.id" >
            <td>{{i.id}}</td>
            <td>{{i.name}}</td>
            <td>{{i.email}}</td>
        </tr>
    </table>
    </div>
</template>
<script>
export default {
        name : 'MyUsers',

        data(){
            return {
            users:[
                {id:1, name: "Raj",email : "raj@gmail.com"},
                {id:2, name: "Rahul",email : "rahul@gmail.com"},
                {id:3, name: "Ram",email : "ram@gmail.com"},
                {id:4, name: "Rajni",email : "rajni@gmail.com"},
            ],
           }
        }
}

</script>

<style>
        .div2{
            height : 300px;
            width : 500px;
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
        .styled-table tr {
            border-bottom: 1px solid #dddddd;
        }

        .styled-table tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }

        .styled-table tr:last-of-type {
            border-bottom: 2px solid #009879;
        }
        .styled-table tr.active-row {
            font-weight: bold;
            color: #009879;
        }

</style>