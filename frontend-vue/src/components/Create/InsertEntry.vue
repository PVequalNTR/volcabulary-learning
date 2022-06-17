<template>
        <router-link :to="ToLocation" class="InsertEntryBtn">{{msg}}</router-link>
</template>

<script>
export default {
    props:{
        msg:{
            type:String,
            default:"預設訊息",
        },
        ToLocation:{
            type:String,
            default:"",
        }
    }
}
</script>

<style>

    .InsertEntryBtn{
        width: 45%;
        margin: 2%;
        height: 25%;
        border-radius: 15px;
        background-color: #4CAF50;
        color: black;
        font-size: 180%;
        font-weight:600;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .InsertEntryBtn:hover{
        border:3px solid;
        border-color: #4CAF50;
        background-color: white;
    }

</style>