<template>
    <div class="emp" >
    <h1>In EmployeeList</h1>
    <div>
    <table class="styled-table" border="1">
        <tr>
            <th>Id</th>
            <th>Name</th>
            <th>Salary</th>
            <th>Age</th>
        </tr>
        <tr v-for="i in list" v-bind:key="i.id" >
            <td>{{i.id}}</td>
            <td>{{i.employee_name}}</td>
            <td>{{i.employee_salary}}</td>
            <td>{{i.employee_age}}</td>
        </tr>
    </table>
    </div>
    </div>
</template>
<script>
import axios from "axios"

export default {
    name: 'EmpList',
    data(){
        return {
            list : undefined
        }
    },
    mounted()
    {
        axios.get('https://dummy.restapiexample.com/api/v1/employees')
        .then(response =>{
            this.list = response.data.data
            console.log(response.data.data)
        })
    }
}
</script>
<style>
        .emp{
            height : 50 %;
            width : 50 %;
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
