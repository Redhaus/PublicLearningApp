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
                    console.log('results: ', data.results);
                    console.log('DATA: ', data);

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
                    console.log('DATA: ', data);
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
                    console.log('DATA: ', data);
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

            console.log('EVENT FILTER: ', event_filter);
            // let endpoint
            let endpoint = `http://127.0.0.1:8000/api/performances/?id=&event_collection=${event_filter}`;
            console.log('FETCH LEXIS ENDPOINT : ', endpoint);

            // if (event_filter) {
// http://127.0.0.1:8000/api/extensions/?event_collection=1

            apiService(endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    console.log('DATA: ', data);
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
            console.log('FETCH LEXIS ENDPOINT : ', endpoint);

            // if (event_filter) {

            apiService(endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    console.log('DATA: ', data);
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
                    console.log('DATA: ', data);
                    commit('setGoals', data);
                })
                .catch((err) => {
                    console.log(err)
                })
        }
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


    },

    modules: {
        lesson_store,
        lexis_store,
        question_store,
    }
});
