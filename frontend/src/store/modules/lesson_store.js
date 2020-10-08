// create state
const state = {
    lesson: {
        selected_event: '',
        selected_reading: '',
        selected_related_events: [],
        selected_exploration: [],
        selected_lexis: [],
        selected_questions: [],
        selected_performances: [],
        selected_extensions: [],
        selected_goals: [],
        user_questions: []

    }
};


// create mutations
const mutations = {
    setSelectedEvent(state, payload) {
        // state.lesson.selected_event = payload

        if (state.lesson.selected_event === payload) {

            state.lesson.selected_event = '';
        } else {
            state.lesson.selected_event = payload
        }

    },

    setSelectedReading(state, payload) {

        if (state.lesson.selected_reading === payload) {
            state.lesson.selected_reading = '';
        } else {
            state.lesson.selected_reading = payload
        }

    },

    setSelectedLexis(state, payload) {
        // setSelectedLexis() {

        // if event is already in array, then remove it with filter
        // otherwise push it to the array
        if (state.lesson.selected_lexis.includes(payload)) {
            state.lesson.selected_lexis = state.lesson.selected_lexis.filter(function (item) {
                return item !== payload;
            });
        } else {
            state.lesson.selected_lexis.push(payload);
        }

        // state.lesson.selected_lexis = payload
    },

    setSelectedExplorations(state, payload) {

        // if event is already in array, then remove it with filter
        // otherwise push it to the array
        if (state.lesson.selected_exploration.includes(payload)) {
            state.lesson.selected_exploration = state.lesson.selected_exploration.filter(function (item) {
                return item !== payload;
            });
        } else {
            state.lesson.selected_exploration.push(payload);
        }

        // state.lesson.selected_lexis = payload
    },

    setSelectedQuestions(state, payload) {

        // if event is already in array, then remove it with filter
        // otherwise push it to the array
        if (state.lesson.selected_questions.includes(payload)) {
            state.lesson.selected_questions = state.lesson.selected_questions.filter(function (item) {
                return item !== payload;
            });
        } else {
            state.lesson.selected_questions.push(payload);
        }

        // state.lesson.selected_lexis = payload
    },

    setSelectedPerformances(state, payload) {

        // if event is already in array, then remove it with filter
        // otherwise push it to the array
        if (state.lesson.selected_performances.includes(payload)) {
            state.lesson.selected_performances = state.lesson.selected_performances.filter(function (item) {
                return item !== payload;
            });
        } else {
            state.lesson.selected_performances.push(payload);
        }

    },

    setSelectedExtensions(state, payload) {

        // if event is already in array, then remove it with filter
        // otherwise push it to the array
        if (state.lesson.selected_extensions.includes(payload)) {
            state.lesson.selected_extensions = state.lesson.selected_extensions.filter(function (item) {
                return item !== payload;
            });
        } else {
            state.lesson.selected_extensions.push(payload);
        }

    },

    setSelectedGoals(state, payload) {


        // if event is already in array, then remove it with filter
        // otherwise push it to the array
        if (state.lesson.selected_goals.includes(payload)) {
            state.lesson.selected_goals = state.lesson.selected_goals.filter(function (item) {
                return item !== payload;
            });
        } else {
            state.lesson.selected_goals.push(payload);
        }

    },

    setUserQuestions(state, payload) {
        state.lesson.user_questions.push(payload);
    },

    deleteUserQuestion(state, payload) {
        console.log('MUTATION DELEYE', payload);
        state.lesson.user_questions = state.lesson.user_questions.filter(function (item) {
            console.log('MUTATION DELEYE ID', item);

            return item.id !== payload;
        });
    },



};

// create actions
const actions = {
    setSelectedEvent({commit}, payload) {
        commit('setSelectedEvent', payload);
    },

    setSelectedReading({commit}, payload) {
        commit('setSelectedReading', payload);
    },

    setSelectedLexis({commit}, payload) {
        commit('setSelectedLexis', payload);
    },

    setSelectedExplorations({commit}, payload) {
        commit('setSelectedExplorations', payload);
    },

    setSelectedQuestions({commit}, payload) {
        commit('setSelectedQuestions', payload);
    },

    setSelectedPerformances({commit}, payload) {
        commit('setSelectedPerformances', payload);
    },

    setSelectedExtensions({commit}, payload) {
        commit('setSelectedExtensions', payload);
    },

    setSelectedGoals({commit}, payload) {
        commit('setSelectedGoals', payload);
    },

    setUserQuestions({commit}, payload) {
        commit('setUserQuestions', payload);
    },
    deleteUserQuestion({commit}, payload) {
        commit('deleteUserQuestion', payload);
    },



};

// create getters
const getters = {
    getSelectedEvent(state) {
        return state.lesson.selected_event;
    },

    getSelectedReading(state) {
        return state.lesson.selected_reading;
    },

    getSelectedLexis(state) {
        return state.lesson.selected_lexis;
    },

    getSelectedExplorations(state) {
        return state.lesson.selected_exploration;
    },

    getSelectedQuestions(state) {
        return state.lesson.selected_questions;
    },

    getSelectedPerformances(state) {
        return state.lesson.selected_performances;
    },

    getSelectedExtensions(state) {
        return state.lesson.selected_extensions;
    },

    getSelectedGoals(state) {
        return state.lesson.selected_goals;
    },

    getSelections(state) {
        console.log('GETTER SELECTIONS', state.lesson);
        return state.lesson
    },

    getUserQuestions(state) {
        // console.log('GETTER SELECTIONS', state.lesson);
        return state.lesson.user_questions
    },

};


// export each object
export default {
    state,
    actions,
    mutations,
    getters
}