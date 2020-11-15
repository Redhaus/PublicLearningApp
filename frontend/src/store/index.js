import Vue from "vue";
import Vuex from "vuex";

import {apiService} from "./api_service";
import {signInService} from "./signin_service";

import lesson_store from "./modules/lesson_store";
import lexis_store from "./modules/lexis_store";
import question_store from "./modules/question_store";
import user_class_store from "./modules/user_class_store";
import router from "../router";

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
        instructorInfo: {}
        // lessons: [],
        // user_classes: [],
        // new_lesson_description: '',
        // new_lesson_class_id: '',
        // new_lesson_title: '',


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

        setInstructor(state, payload){
            console.log('USER', payload);

             state.instructorInfo = payload


        },

        // // saves new lesson to lesson list in vuex store
        // saveLesson(state, payload) {
        //     // console.log('SAVE LESSON PAYLOAD', payload);
        //
        //     var title = payload.lesson_title;
        //
        //     var lesson = JSON.parse(payload.lesson_selections);
        //
        //     var lexis = lesson.selected_lexis;
        //     var event = lesson.selected_event;
        //     var explorations = lesson.selected_exploration;
        //     var extensions = lesson.selected_extensions;
        //     var goals = lesson.selected_goals;
        //     var performances = lesson.selected_performances;
        //     var questions = lesson.selected_questions;
        //     var readings = lesson.selected_reading;
        //     var user_questions = lesson.selected_reading;
        //
        //
        //     let data = {
        //         'id': payload.id,
        //         'lesson_title': title,
        //         'lexis': lexis,
        //         'event': event,
        //         'explorations': explorations,
        //         'extensions': extensions,
        //         'goals': goals,
        //         'performances': performances,
        //         'questions': questions,
        //         'readings': readings,
        //         'user_questions': user_questions
        //     };
        //
        //
        //     state.lessons.unshift(data)
        //
        // },
        //
        // setLessonTitle(state, payload) {
        //
        //     state.new_lesson_title = payload.title;
        //     state.new_lesson_description = payload.description;
        //     state.new_lesson_class_id = payload.class_id;
        //
        // },
        //
        // // sets all lessons on initial load
        // setLessons(state, payload) {
        //
        //     // console.log("LESSONPAYLOAD ", payload);
        //
        //     // state.lessons = payload;
        //
        //     state.lessons = [];
        //
        //     // foreach(payload)
        //     payload.forEach(element => {
        //
        //         // console.log("PAYLOADELEMENT ", element);
        //         var title = element.lesson_title;
        //         var description = element.lesson_description;
        //         var class_link = element.class_link;
        //
        //
        //         var lesson = JSON.parse(element.lesson_selections);
        //
        //         // console.log("LESSON", lesson);
        //
        //         var lexis = lesson.selected_lexis;
        //         var event = lesson.selected_event;
        //         var explorations = lesson.selected_exploration;
        //         var extensions = lesson.selected_extensions;
        //         var goals = lesson.selected_goals;
        //         var performances = lesson.selected_performances;
        //         var questions = lesson.selected_questions;
        //         var readings = lesson.selected_reading;
        //         var user_questions = lesson.user_questions;
        //
        //
        //         let data = {
        //             'id': element.id,
        //             'lesson_title': title,
        //             'lesson_description': description,
        //             'class_link': class_link,
        //             'lexis': lexis,
        //             'event': event,
        //             'explorations': explorations,
        //             'extensions': extensions,
        //             'goals': goals,
        //             'performances': performances,
        //             'questions': questions,
        //             'readings': readings,
        //             'user_questions': user_questions,
        //         };
        //
        //         // console.log("DATA ", data);
        //         // console.log("LEXIS ", lexis);
        //
        //         state.lessons.push(data)
        //
        //
        //     });
        //     // state.lessons = payload
        // },
        //
        // saveClass(state, payload) {
        //     state.user_classes.push(payload)
        // },
        //
        // updateClass(state, payload) {
        //
        //     const index = state.user_classes.findIndex(x => x.id === payload.id);
        //     state.user_classes.splice(index, 1, payload);
        //     // state.user_classes.findIndex((el) => el === 1) !== -1;
        //     // state.user_classes.push(payload)
        // },
        //
        // setClasses(state, payload) {
        //     state.user_classes = payload;
        // },
        //
        // deleteUserClass(state, payload) {
        //     // console.log('MUTATION DELETE', payload);
        //     state.user_classes = state.user_classes.filter(function (item) {
        //         // console.log('MUTATION DELEYE ID', item);
        //
        //         return item.id !== payload;
        //     });
        // },

        // deleteUserLesson(state, payload) {
        //     // console.log('MUTATION DELETE', payload);
        //     state.lessons = state.lessons.filter(function (item) {
        //         // console.log('MUTATION DELEYE ID', item);
        //         return item.id !== payload;
        //     });
        // },
        //
        // clearLessonSelections(state) {
        //
        //
        //     state.lesson_store.lesson.selected_event = '';
        //     state.lesson_store.lesson.selected_reading = '';
        //     state.lesson_store.lesson.selected_related_events = [];
        //     state.lesson_store.lesson.selected_exploration = [];
        //     state.lesson_store.lesson.selected_lexis = [];
        //     state.lesson_store.lesson.selected_questions = [];
        //     state.lesson_store.lesson.selected_performances = [];
        //     state.lesson_store.lesson.selected_extensions = [];
        //     state.lesson_store.lesson.selected_goals = [];
        //     state.lesson_store.lesson.user_questions = []
        //
        //
        // },
        //
        // setEditLesson(state, payload) {
        //
        //     state.new_lesson_description = payload.new_lesson_description,
        //     state.new_lesson_class_id = payload.new_lesson_class_id,
        //     state.new_lesson_title = payload.new_lesson_title,
        //
        //     state.lesson_store.lesson = {
        //         selected_event: payload.event,
        //         selected_reading: payload.readings,
        //         selected_related_events: [],
        //         selected_exploration: payload.explorations,
        //         selected_lexis: payload.lexis,
        //         selected_questions: payload.questions,
        //         selected_performances: payload.performances,
        //         selected_extensions: payload.extensions,
        //         selected_goals: payload.goals,
        //         user_questions: payload.user_questions,
        //     }
        // }


    },

    actions: {

        // setSelectedEvent({commit}, payload) {
        //     commit('setSelectedEvent', payload);
        // },

        fetchEvents({commit}) {

            let endpoint = 'http://127.0.0.1:8000/api/event_overviews/';

            // fetchEvents({commit}, {endpoint}) {
            // relative pass because fetch populates base url  automatically
            // console.log('FETCH CALLED: ');
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
            // let event_filter = state.lesson_store.getters['getSelectedEvent'];

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
            // console.log('EVENT FILTER: ', event_filter);

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
            // console.log('FETCH GOAL ENDPOINT : ', endpoint);

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


        // fetchLessons({commit}, id) {
        //
        //     // let class_endpoint = `http://127.0.0.1:8000/api/class_name/?instructor=${id}`;
        //     // let lesson_endpoint = "http://127.0.0.1:8000/api/user_lessons/";
        //     let lesson_endpoint = `http://127.0.0.1:8000/api/user_lessons/?instructor=${id}`;
        //
        //
        //     apiService(lesson_endpoint)
        //         .then(data => {
        //             // console.log('results: ', data.results);
        //             // console.log('DATA: ', data);
        //             commit('setLessons', data);
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //         });
        //
        // },
        //
        // postLessonTitle({commit}, payload) {
        //     commit('setLessonTitle', payload);
        // },

        //
        // postNewClass({commit, state}, payload) {
        //
        //     // instructor is being added via serializer from user logged in
        //
        //     let class_endpoint = "http://127.0.0.1:8000/api/class_name/";
        //
        //     // console.log('DATAPAYLOAD: ', payload);
        //
        //     let classData = {
        //         "class_name": payload.class_name,
        //         "grade_level": payload.grade_level,
        //         "class_description": payload.class_description
        //     };
        //
        //     // console.log('DATAPAYLOAD: ', classData);
        //
        //
        //     apiService(class_endpoint, "POST", classData)
        //         .then(data => {
        //             // console.log('results: ', data.results);
        //             // console.log('DATA: ', data);
        //             // commit('postLesson', data);
        //             commit('saveClass', data);
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //         });
        // },
        //
        // updateClass({commit, state}, payload) {
        //
        //     // instructor is being added via serializer from user logged in
        //
        //     // let class_endpoint = "http://127.0.0.1:8000/api/class_name/";
        //     let class_endpoint = `http://127.0.0.1:8000/api/class_name/${payload.id}/`;
        //
        //     // console.log('DATAPAYLOAD: ', payload);
        //
        //     let classData = {
        //         "class_name": payload.class_name,
        //         "grade_level": payload.grade_level,
        //         "class_description": payload.class_description
        //     };
        //
        //     // console.log('DATAPAYLOAD: ', classData);
        //
        //
        //     apiService(class_endpoint, "PUT", classData)
        //         .then(data => {
        //             // console.log('results: ', data.results);
        //             // console.log('DATA: ', data);
        //             // commit('postLesson', data);
        //             commit('updateClass', data);
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //         });
        // },

        //
        // postLesson({commit, state}) {
        //
        //
        //     // instructor is being added via serializer from user logged in
        //
        //     let lesson_endpoint = "http://127.0.0.1:8000/api/user_lessons/";
        //
        //     // console.log('POST PAYLOAD', state.lesson_store.lesson);
        //     // var myJSON = JSON.stringify(obj);
        //     let lessonData = {
        //         "instructor": {},
        //         "lesson_title": state.new_lesson_title,
        //         "lesson_selections": JSON.stringify(state.lesson_store.lesson),
        //         "class_link": state.new_lesson_class_id,
        //         "lesson_description": state.new_lesson_description
        //     };
        //
        //     // console.log('POST STRING', lessonData.lesson_selections);
        //
        //     // const apiService = function (endpoint, method, data) {
        //     apiService(lesson_endpoint, "POST", lessonData)
        //         .then(data => {
        //             // console.log('results: ', data.results);
        //             console.log('DATA: ', data);
        //             // commit('postLesson', data);
        //             commit('saveLesson', data);
        //         })
        //         .then(data => {
        //             commit('clearLessonSelections')
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //         });
        //
        // },


        signoutFunction() {

            let signout_endpoint = "http://127.0.0.1:8000/rest-auth/logout/";

            signInService(signout_endpoint, "GET")
                .then(data => {

                    window.localStorage.removeItem('access_token');
                    window.localStorage.removeItem('user');
                    window.localStorage.removeItem('user_id');
                    window.localStorage.removeItem('instructor_id');

                    router.push("/signin");

                    console.log('SIGNOUT', data);
                })

                .catch((err) => {
                    console.log(err)
                });

        },



        signinFunction(context, {username, password}) {

            let signin_endpoint = "http://127.0.0.1:8000/rest-auth/login/";

            // console.log('context', context);
            // console.log('USERNAME PAYLOAD', username);
            // console.log('PASSWORD DATA', password);

            // var myJSON = JSON.stringify(obj);
            let loginData = {
                "username": username,
                "password": password
            };

            // console.log('POST STRING', lessonData.lesson_selections);

            // const apiService = function (endpoint, method, data) {
            signInService(signin_endpoint, "POST", loginData)
                .then(data => {

                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);

                    window.localStorage.setItem('access_token', data.token);
                    window.localStorage.setItem('user', data.user);
                    window.localStorage.setItem('user_id', data.id);
                    window.localStorage.setItem('instructor_id', data.instructor_id);
                    // self.router.push('/');
                    router.push("/dashboard");

                    // commit('postLesson', data);
                })

                .catch((err) => {
                    console.log(err)
                });

        },
        //
        // fetchClasses({commit}, id) {
        //
        //     // let id =
        //     // let event_filter = state.lesson_store.lesson.selected_event;
        //     // console.log('EVENT FILTER: ', event_filter);
        //
        //     // console.log('EVENT FILTER: ', event_filter);
        //     // let endpoint = 'http://127.0.0.1:8000/api/questions/';
        //     // let endpoint = `http://127.0.0.1:8000/api/extensions/?event_collection=${event_filter}`;
        //     // console.log('FETCH LEXIS ENDPOINT : ', endpoint);
        //
        //
        //     let class_endpoint = `http://127.0.0.1:8000/api/class_name/?instructor=${id}`;
        //
        //
        //     apiService(class_endpoint)
        //         .then(data => {
        //             // console.log('results: ', data.results);
        //             // console.log('DATA: ', data);
        //             commit('setClasses', data);
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //         });
        //
        // },
        //
        // deleteUserClass({commit}, payload) {
        //
        //     let class_endpoint = `http://127.0.0.1:8000/api/class_name/${payload}/`;
        //
        //     apiService(class_endpoint, "DELETE")
        //         .then(data => {
        //
        //             // console.log('results: ', data.results);
        //             // console.log('DATA: ', data);
        //
        //             // commit('postLesson', data);
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //         });
        //
        //     commit('deleteUserClass', payload);
        // },


        // deleteUserLesson({state, dispatch}, payload) {
        //
        //     let class_endpoint = `http://127.0.0.1:8000/api/user_lessons/${payload}/`;
        //
        //     apiService(class_endpoint, "DELETE")
        //         .then(data => {
        //
        //             // console.log('results: ', data.results);
        //             // console.log('DATA: ', data);
        //             // commit('postLesson', data);
        //
        //
        //             let id = window.localStorage.getItem('instructor_id');
        //             console.log('ID', id);
        //
        //             console.log('DATA', data);
        //
        //             dispatch('fetchLessons', id);
        //             // dispatch('deleteUserClass', id)
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //         });
        //
        //     // commit('deleteUserLesson', payload);
        // },
        //
        // editLesson({commit}, payload) {
        //     commit('setEditLesson', payload);
        // }


        fetchInstructor({commit}) {

            let teacherID = window.localStorage.getItem('instructor_id');
             console.log('TEACHER ID', teacherID);


            let endpoint = `http://127.0.0.1:8000/api/teacher_profile/${teacherID}/`;

              console.log('TEACHER ENDPOINT', endpoint);

            apiService(endpoint)
                .then(data => {
                    commit('setInstructor', data);
                })
                .catch((err) => {
                    console.log(err)
                })
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
            // console.log('GET Extensions CALLED');
            return state.extension_categories
        },

        getReadingCategories(state) {
            // console.log('GET READINGS CALLED');
            return state.reading_categories
        },

        getInstructor(state) {
            return state.instructorInfo
        },


    },

    modules: {
        lesson_store,
        lexis_store,
        question_store,
        user_class_store
    }
});