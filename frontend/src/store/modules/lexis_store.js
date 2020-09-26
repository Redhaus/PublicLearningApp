// create state
import {apiService} from "../api_service";

const state = {
    lexis: [],
};


// create mutations
const mutations = {
    setLexis(state, payload) {
        state.lexis = payload
    },
};

// create actions
const actions = {

    fetchLexis({commit, rootState}) {
        // console.log('STATE: ', state);
        // console.log('ROOTSTATE: ', rootState);

            //http://127.0.0.1:8000/api/lexis/?term=&event_collection=&related_events__event_link=2

        // /cars/color:blue/type:sedan/doors:4

// http://127.0.0.1:8000/api/lexis/event_collection:1/related_events__event_link:1
// http://127.0.0.1:8000/api/lexis/?term=&event_collection=1&related_events__event_link=1

            // rootState
            let event_filter = rootState.lesson_store.lesson.selected_event;
        // let event_filter = rootState.lesson.selected_event;

            let endpoint = `http://127.0.0.1:8000/api/lexis/?term=&event_collection=${event_filter}`;
            // console.log('FETCH LEXIS ENDPOINT : ', endpoint);

            // if (event_filter) {


            apiService(endpoint)
                .then(data => {
                    // console.log('results: ', data.results);
                    // console.log('DATA: ', data);
                    commit('setLexis', data);
                })
                .catch((err) => {
                    console.log(err)
                })


    },
};

// create getters
const getters = {
    getLexis(state) {
        return state.lexis
    },
};


// export each object
export default {
    state,
    actions,
    mutations,
    getters
}