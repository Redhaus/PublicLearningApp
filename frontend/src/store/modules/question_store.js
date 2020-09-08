// create state
import {apiService} from "../api_service";

const state = {
    questions: [],
};


// create mutations
const mutations = {
    setQuestions(state, payload) {
        state.questions = payload
    },
};

// create actions
const actions = {


        //   let event_filter = rootState.lesson_store.lesson.selected_event;
        // console.log('EVENT FILTER: ', event_filter);
        // // let endpoint = 'http://127.0.0.1:8000/api/lexis/';
        // let endpoint = `http://127.0.0.1:8000/api/lexis/?term=&event_collection=${event_filter}`;
        // console.log('FETCH LEXIS ENDPOINT : ', endpoint);
        //

    fetchQuestions({commit, rootState}) {
        let event_filter = rootState.lesson_store.lesson.selected_event;
        // console.log('EVENT FILTER: ', event_filter);
        // let endpoint = 'http://127.0.0.1:8000/api/questions/';
        let endpoint = `http://127.0.0.1:8000/api/questions/?event_collection=${event_filter}`;
        console.log('FETCH LEXIS ENDPOINT : ', endpoint);


        apiService(endpoint)
            .then(data => {
                // console.log('results: ', data.results);
                console.log('DATA: ', data);
                commit('setQuestions', data);
            })
            .catch((err) => {
                console.log(err)
            })
    },

};

// create getters
const getters = {
    getQuestions(state) {
        return state.questions
    },
};


// export each object
export default {
    state,
    actions,
    mutations,
    getters
}