<template>

    <div>

        <h5 class="redOne">lesson title</h5>
        <p class="blueOne">{{ lesson.lesson_title }}</p>
        <h5 class="redOne">lesson description</h5>
        <p class="blueOne">{{lesson.lesson_description}}</p>





    </div>

</template>

<script>
    export default {
        name: "testLesson.vue",
        props: ['lesson'],



        created() {
            console.log('LESSON INFO IN TEST', this.lesson);
            console.log('LESSON TITLE', this.lesson.lesson_title)

        },

        methods: {

        }

    }

</script>

<style scoped>
    .redOne {
        color: red;
    }

    .blueOne {
        color: blue;
        font-size: 9px;
    }

</style>