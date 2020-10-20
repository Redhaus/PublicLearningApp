// create state
import {apiService} from "../api_service";

const state = {
     user_classes: [],
};


// create mutations
const mutations = {


        saveClass(state, payload) {
            state.user_classes.push(payload)
        },

        updateClass(state, payload) {
            const index = state.user_classes.findIndex(x => x.id === payload.id);
            state.user_classes.splice(index, 1, payload);
            // state.user_classes.findIndex((el) => el === 1) !== -1;
            // state.user_classes.push(payload)
        },

        setClasses(state, payload) {
            state.user_classes = payload;
        },

        deleteUserClass(state, payload) {
            // console.log('MUTATION DELETE', payload);
            state.user_classes = state.user_classes.filter(function (item) {
                // console.log('MUTATION DELEYE ID', item);
                return item.id !== payload;
            });
        },



};

// create actions
const actions = {



        postNewClass({commit, state}, payload) {

            // instructor is being added via serializer from user logged in

            let class_endpoint = "http://127.0.0.1:8000/api/class_name/";

            // console.log('DATAPAYLOAD: ', payload);

            let classData = {
                "class_name": payload.class_name,
                "grade_level": payload.grade_level,
                "class_description": payload.class_description
            };

            // console.log('DATAPAYLOAD: ', classData);


            apiService(class_endpoint, "POST", classData)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    // commit('postLesson', data);
                    commit('saveClass', data);
                })
                .catch((err) => {
                    console.log(err)
                });
        },

        updateClass({commit, state}, payload) {

            // instructor is being added via serializer from user logged in

            // let class_endpoint = "http://127.0.0.1:8000/api/class_name/";
            let class_endpoint = `http://127.0.0.1:8000/api/class_name/${payload.id}/`;


            let classData = {
                "class_name": payload.class_name,
                "grade_level": payload.grade_level,
                "class_description": payload.class_description
            };



            apiService(class_endpoint, "PUT", classData)
                .then(data => {

                    commit('updateClass', data);
                })
                .catch((err) => {
                    console.log(err)
                });
        },




        fetchClasses({commit}, id) {

            // let id =
            // let event_filter = state.lesson_store.lesson.selected_event;
            // console.log('EVENT FILTER: ', event_filter);

            // console.log('EVENT FILTER: ', event_filter);
            // let endpoint = 'http://127.0.0.1:8000/api/questions/';
            // let endpoint = `http://127.0.0.1:8000/api/extensions/?event_collection=${event_filter}`;
            // console.log('FETCH LEXIS ENDPOINT : ', endpoint);


            let class_endpoint = `http://127.0.0.1:8000/api/class_name/?instructor=${id}`;


            apiService(class_endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setClasses', data);
                })
                .catch((err) => {
                    console.log(err)
                });

        },

        deleteUserClass({commit}, payload) {

            let class_endpoint = `http://127.0.0.1:8000/api/class_name/${payload}/`;

            apiService(class_endpoint, "DELETE")
                .then(data => {

                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);

                    // commit('postLesson', data);
                })
                .catch((err) => {
                    console.log(err)
                });

            commit('deleteUserClass', payload);
        },



};

// create getters
const getters = {

        getUserClasses(state) {
            return state.user_classes
        },

};


// export each object
export default {
    state,
    actions,
    mutations,
    getters
}