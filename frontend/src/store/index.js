import Vue from "vue";
import Vuex from "vuex";

import {apiService} from "./api_service";
import lesson_store from "./modules/lesson_store";
import lexis_store from "./modules/lexis_store";
import question_store from "./modules/question_store";


Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        events: [],
        readings: [],
        explorations: [],
        // questions: null,
        performances: [],
        extensions: [],
        goals: [],
        goal_categories: [],
        extension_categories: [],
        reading_categories: [],
        lessons: [],
        new_lesson_title: ''


    },


    mutations: {

        setEvents(state, payload) {
            state.events = payload
        },

        setReadings(state, payload) {
            state.readings = payload
        },

        setExplorations(state, payload) {
            state.explorations = payload
        },

        // setQuestions(state, payload) {
        //     state.questions = payload
        // },

        setPerformances(state, payload) {
            state.performances = payload
        },

        setExtensions(state, payload) {
            state.extensions = payload
        },

        setGoals(state, payload) {
            state.goals = payload
        },

        setGoalCategories(state, payload) {
            state.goal_categories = payload
        },

        setExtensionCategories(state, payload) {
            state.extension_categories = payload
        },

        setReadingCategories(state, payload) {
            state.reading_categories = payload
        },

        // saves new lesson to lesson list in vuex store
        saveLesson(state,payload){
            console.log('SAVE LESSON PAYLOAD' , payload);

            var title = payload.lesson_title;

                var lesson = JSON.parse(payload.lesson_selections);

                var lexis = lesson.selected_lexis;
                var event = lesson.selected_event;
                var explorations = lesson.selected_exploration;
                var extensions = lesson.selected_extensions;
                var goals = lesson.selected_goals;
                var performances = lesson.selected_performances;
                var questions = lesson.selected_questions;
                var readings = lesson.selected_reading;


                let data = {
                    'id': payload.id,
                    'lesson_title' : title,
                    'lexis' : lexis,
                    'event': event,
                    'explorations': explorations,
                    'extensions': extensions,
                    'goals': goals,
                    'performances': performances,
                    'questions': questions,
                    'readings': readings,
                };


                state.lessons.unshift(data)

        },

        setLessonTitle(state, payload) {
            state.new_lesson_title = payload;
        },

        // sets all lessons on initial load
        setLessons(state, payload) {

            console.log("LESSONPAYLOAD ", payload);

            // state.lessons = payload;

            state.lessons = [];

            // foreach(payload)
            payload.forEach(element => {

                console.log("PAYLOADELEMENT ", element);
                var title = element.lesson_title;

                var lesson = JSON.parse(element.lesson_selections);

                var lexis = lesson.selected_lexis;
                var event = lesson.selected_event;
                var explorations = lesson.selected_exploration;
                var extensions = lesson.selected_extensions;
                var goals = lesson.selected_goals;
                var performances = lesson.selected_performances;
                var questions = lesson.selected_questions;
                var readings = lesson.selected_reading;


                let data = {
                    'id': element.id,
                    'lesson_title' : title,
                    'lexis' : lexis,
                    'event': event,
                    'explorations': explorations,
                    'extensions': extensions,
                    'goals': goals,
                    'performances': performances,
                    'questions': questions,
                    'readings': readings,
                };

                // console.log("DATA ", data);
                // console.log("LEXIS ", lexis);

                state.lessons.push(data)


            });
            // state.lessons = payload
        },




    },

    actions: {

        // setSelectedEvent({commit}, payload) {
        //     commit('setSelectedEvent', payload);
        // },

        fetchEvents({commit}) {

            let endpoint = 'http://127.0.0.1:8000/api/event_overviews/';

            // fetchEvents({commit}, {endpoint}) {
            // relative pass because fetch populates base url  automatically
            console.log('FETCH CALLED: ');
            apiService(endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);

                    commit('setEvents', data);
                })
                .catch((err) => {
                    console.log(err)
                })

        },

        fetchReadings({commit, state}) {

            let event_filter = state.lesson_store.lesson.selected_event;
            let endpoint = `http://127.0.0.1:8000/api/primary_focus/?event_collection=${event_filter}`;


            // let endpoint = 'http://127.0.0.1:8000/api/primary_focus/';
            apiService(endpoint)
                .then(data => {
                    // console.log('DATA: ', data);
                    commit('setReadings', data);
                })
                .catch((err) => {
                    console.log(err)
                })

        },

        fetchExplorations({commit, state}) {
            let event_filter = state.lesson_store.lesson.selected_event;
            let endpoint = `http://127.0.0.1:8000/api/further_explorations/?event_collection=${event_filter}`;

            apiService(endpoint)
                .then(data => {
                    // console.log('DATA: ', data);
                    commit('setExplorations', data);
                })
                .catch((err) => {
                    console.log(err)
                })

        },


        // fetchQuestions({commit, state}) {
        //     let event_filter = state.lesson_store.lesson.selected_event;
        //     // console.log('EVENT FILTER: ', event_filter);
        //     // let endpoint = 'http://127.0.0.1:8000/api/questions/';
        //     let endpoint = `http://127.0.0.1:8000/api/questions/?event_collection=${event_filter}`;
        //     console.log('FETCH LEXIS ENDPOINT : ', endpoint);
        //
        //     // if (event_filter) {
        //
        //
        //     apiService(endpoint)
        //         .then(data => {
        //             // console.log('results: ', data.results);
        //             console.log('DATA: ', data);
        //             commit('setQuestions', data);
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //         })
        // },

        fetchPerformances({commit, state}) {
            let event_filter = state.lesson_store.lesson.selected_event;

            // console.log('EVENT FILTER: ', event_filter);
            // let endpoint
            let endpoint = `http://127.0.0.1:8000/api/performances/?id=&event_collection=${event_filter}`;
            // console.log('FETCH LEXIS ENDPOINT : ', endpoint);

            // if (event_filter) {
// http://127.0.0.1:8000/api/extensions/?event_collection=1

            apiService(endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setPerformances', data);
                })
                .catch((err) => {
                    console.log(err)
                })
        },

        fetchExtensions({commit, state}) {
            let event_filter = state.lesson_store.lesson.selected_event;
            console.log('EVENT FILTER: ', event_filter);

            // console.log('EVENT FILTER: ', event_filter);
            // let endpoint = 'http://127.0.0.1:8000/api/questions/';
            let endpoint = `http://127.0.0.1:8000/api/extensions/?event_collection=${event_filter}`;
            // console.log('FETCH LEXIS ENDPOINT : ', endpoint);

            // if (event_filter) {

            apiService(endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setExtensions', data);
                })
                .catch((err) => {
                    console.log(err)
                })
        },

        fetchGoals({commit}) {


            let endpoint = "http://127.0.0.1:8000/api/goals/";
            console.log('FETCH GOAL ENDPOINT : ', endpoint);

            // if (event_filter) {

            apiService(endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setGoals', data);
                })
                .catch((err) => {
                    console.log(err)
                })
        },

        fetchCategories({commit}) {

            let reading_cat_endpoint = "http://127.0.0.1:8000/api/reading_categories/";
            let extension_cat_endpoint = "http://127.0.0.1:8000/api/extension_categories/";
            let goal_cat_endpoint = "http://127.0.0.1:8000/api/goal_categories/";

            // let endpoint = "http://127.0.0.1:8000/api/goals/";
            // console.log('FETCH GOAL ENDPOINT : ', endpoint);

            // if (event_filter) {

            apiService(reading_cat_endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setReadingCategories', data);
                })
                .catch((err) => {
                    console.log(err)
                });

            apiService(extension_cat_endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setExtensionCategories', data);
                })
                .catch((err) => {
                    console.log(err)
                });

            apiService(goal_cat_endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setGoalCategories', data);
                })
                .catch((err) => {
                    console.log(err)
                })
        },


        fetchLessons({commit}) {

            let lesson_endpoint = "http://127.0.0.1:8000/api/user_lessons/";


            apiService(lesson_endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setLessons', data);
                })
                .catch((err) => {
                    console.log(err)
                });

        },

        postLessonTitle({commit}, payload){
            commit('setLessonTitle', payload);
        },

        postLesson({commit, state}) {

            let lesson_endpoint = "http://127.0.0.1:8000/api/user_lessons/";

            console.log('POST PAYLOAD', state.lesson_store.lesson);
            // var myJSON = JSON.stringify(obj);
            let lessonData = {
                "instructor": {},
                "lesson_title": state.new_lesson_title,
                "lesson_selections": JSON.stringify(state.lesson_store.lesson)
                // "lesson_selections": payload.state.lesson_store.lesson

            };

            console.log('POST STRING', lessonData.lesson_selections);

            // const apiService = function (endpoint, method, data) {
            apiService(lesson_endpoint, "POST", lessonData)
                .then(data => {
                    // console.log('results: ', data.results);
                    console.log('DATA: ', data);
                    // commit('postLesson', data);
                     commit('saveLesson', data);
                })
                .catch((err) => {
                    console.log(err)
                });

        },


        signinFunction(context, {username, password}) {

            let signin_endpoint = "http://127.0.0.1:8000/rest-auth/login/";

            console.log('context', context);
            console.log('USERNAME PAYLOAD', username);
            console.log('PASSWORD DATA', password);

            // var myJSON = JSON.stringify(obj);
            let loginData = {
                "username": username,
                "password": password
            };

            // console.log('POST STRING', lessonData.lesson_selections);

            // const apiService = function (endpoint, method, data) {
            apiService(signin_endpoint, "POST", loginData)
                .then(data => {

                    // console.log('results: ', data.results);
                    console.log('DATA: ', data);

                    window.localStorage.setItem('access_token', data.token);
                    window.localStorage.setItem('user', data.user);
                    window.localStorage.setItem('user_id', data.id);



                    // commit('postLesson', data);
                })
                .catch((err) => {
                    console.log(err)
                });

        },




    },

    getters: {

        getEvents(state) {
            return state.events
        },

        getReadings(state) {
            return state.readings
        },

        getExplorations(state) {
            return state.explorations
        },

        getPerformances(state) {
            return state.performances
        },

        getExtensions(state) {
            return state.extensions
        },

        getGoals(state) {
            return state.goals
        },

        getGoalCategories(state) {
            return state.goal_categories
        },

        getExtensionCategories(state) {
            console.log('GET Extensions CALLED');
            return state.extension_categories
        },

        getReadingCategories(state) {
            console.log('GET READINGS CALLED');
            return state.reading_categories
        },

        getLessons(state) {
            return state.lessons
        },




    },

    modules: {
        lesson_store,
        lexis_store,
        question_store,
    }
});
