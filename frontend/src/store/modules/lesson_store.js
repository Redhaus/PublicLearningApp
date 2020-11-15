// create state
import {apiService} from "../api_service";

const state = {

    lessons: [],
    new_lesson_description: '',
    new_lesson_class_id: '',
    new_lesson_title: '',
    lesson_id: '',
    is_editing: false,
    is_duplicate: false,
    is_new: false,
    seamlessSave: false,

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

    // SET STORE LESSON SECTION DATA
    setSelectedEvent(state, payload) {
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

    // DELETE STORE ITEMS MUTATIONS
    // Removes user questions
    deleteUserQuestion(state, payload) {
        state.lesson.user_questions = state.lesson.user_questions.filter(function (item) {
            return item.id !== payload;
        });
    },

    // removes user question from lessons array on delete
    deleteUserLesson(state, payload) {
        // console.log('MUTATION DELETE', payload);
        state.lessons = state.lessons.filter(function (item) {
            // console.log('MUTATION DELEYE ID', item);
            return item.id !== payload;
        });
    },


    // SAVE MUTATIONS


    // sets all lessons on to lessons list on load
    setLessons(state, payload) {

        state.lessons = [];

        payload.forEach(element => {

            var title = element.lesson_title;
            var description = element.lesson_description;
            var class_link = element.class_link;

            var lesson = JSON.parse(element.lesson_selections);

            var lexis = lesson.selected_lexis;
            var event = lesson.selected_event;
            var explorations = lesson.selected_exploration;
            var extensions = lesson.selected_extensions;
            var goals = lesson.selected_goals;
            var performances = lesson.selected_performances;
            var questions = lesson.selected_questions;
            var readings = lesson.selected_reading;
            var user_questions = lesson.user_questions;

            let data = {
                'id': element.id,
                'lesson_title': title,
                'lesson_description': description,
                'class_link': class_link,
                'lexis': lexis,
                'event': event,
                'explorations': explorations,
                'extensions': extensions,
                'goals': goals,
                'performances': performances,
                'questions': questions,
                'readings': readings,
                'user_questions': user_questions,
            };

            state.lessons.push(data)

        });
    },


    // saves newly created lesson to lessons list in store so it adds to list items on dashboard
    saveLesson(state, payload) {

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
        var user_questions = lesson.selected_reading;


        let data = {
            'id': payload.id,
            'lesson_title': title,
            'lexis': lexis,
            'event': event,
            'explorations': explorations,
            'extensions': extensions,
            'goals': goals,
            'performances': performances,
            'questions': questions,
            'readings': readings,
            'user_questions': user_questions
        };


        state.lessons.unshift(data);
        state.is_editing = false;

    },


    // create new lesson saves title, description and class id to lesson store and sets editing to false
    setLessonTitle(state, payload) {
        state.new_lesson_title = payload.title;
        state.new_lesson_description = payload.description;
        state.new_lesson_class_id = payload.class_id;
        state.is_editing = false;
        state.is_duplicate = false;

    },


    // sets all values on lesson_store.lesson when edit is selected
    setEditLesson(state, payload) {
        // console.log('SETEDITPAYLOAD', payload);
            state.is_editing = true;
            state.is_duplicate = false;


            state.new_lesson_description = payload.lesson_description,
            state.new_lesson_class_id = payload.class_link,
            state.new_lesson_title = payload.lesson_title,
            state.lesson_id = payload.id,

            state.lesson = {
                selected_event: payload.event,
                selected_reading: payload.readings,
                selected_related_events: [],
                selected_exploration: payload.explorations,
                selected_lexis: payload.lexis,
                selected_questions: payload.questions,
                selected_performances: payload.performances,
                selected_extensions: payload.extensions,
                selected_goals: payload.goals,
                user_questions: payload.user_questions,
            }
    },

    // Sets all values on lesson_store.lesson when duplicate is selected
    setDuplicateLesson(state, payload) {

            state.is_duplicate = true;
            state.is_editing = false;

            state.new_lesson_description = payload.lesson_description,
            state.new_lesson_class_id = payload.class_link,
            state.new_lesson_title = payload.lesson_title,
            // state.lesson_id = payload.id,

            state.lesson = {
                selected_event: payload.event,
                selected_reading: payload.readings,
                selected_related_events: [],
                selected_exploration: payload.explorations,
                selected_lexis: payload.lexis,
                selected_questions: payload.questions,
                selected_performances: payload.performances,
                selected_extensions: payload.extensions,
                selected_goals: payload.goals,
                user_questions: payload.user_questions,
            }
    },

    // sets class_id, title and description on review page edit
    setEditLessonData(state, payload) {
        console.log('SETEDITPAYLOAD', payload);
        if (payload.lesson_description) state.new_lesson_description = payload.lesson_description;
        if (payload.class_link) state.new_lesson_class_id = payload.class_link;
        if (payload.lesson_title) state.new_lesson_title = payload.lesson_title
    },

    // once lesson is updated this replaces it in lessons list array
    // removes editing mode
    updateLesson(state, payload) {
        const index = state.lessons.findIndex(x => x.id === payload.id);
        state.lessons.splice(index, 1, payload);
        // state.is_editing = false;
    },

    seamlessSave(state){
        state.seamlessSave = true;
    },

    seamlessSaveOff(state){
        state.seamlessSave = false;
    },

    setLessonID(state,payload){
        state.lesson_id = payload.id;
    },


    // CLEAR MUTATIONS

    // clear all selections from lesson
    clearLessonSelections(state) {
        state.lesson.selected_event = '';
        state.lesson.selected_reading = '';
        state.lesson.selected_related_events = [];
        state.lesson.selected_exploration = [];
        state.lesson.selected_lexis = [];
        state.lesson.selected_questions = [];
        state.lesson.selected_performances = [];
        state.lesson.selected_extensions = [];
        state.lesson.selected_goals = [];
        state.lesson.user_questions = [];
        state.lesson_id = '';

        state.is_duplicate = false;
        state.is_editing = false;
        state.new_lesson_description = '';
        state.new_lesson_class_id = '';
        state.new_lesson_title = '';
    },

    // clears editing mode
    clearIsEditing(state) {
        state.is_editing = false;
    },

    // clears duplicate mode
    clearIsDuplicate(state) {
        state.is_duplicate = false;
    },

    setIsEditing(state){
        state.is_editing = true;
    },


    setIsNew(state){
        state.is_new = true;
    },

    clearIsNew(state){
        state.is_new = false;
    }


    // enables duplicate mode
    // setIsDuplicate(state) {
    //     state.is_duplicate = true;
    // }


};

// create actions
const actions = {

    // SET STORE SECTION SELECTIONS////////////
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


    // GET ACTIONS

    // gets all lesson by logged in user
    fetchLessons({commit}, id) {
        // let class_endpoint = `http://127.0.0.1:8000/api/class_name/?instructor=${id}`;
        // let lesson_endpoint = "http://127.0.0.1:8000/api/user_lessons/";
        let lesson_endpoint = `http://127.0.0.1:8000/api/user_lessons/?instructor=${id}`;

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


    // DELETE ACTIONS
    // DELETE USER QUESTION FROM STORE
    deleteUserQuestion({commit}, payload) {
        commit('deleteUserQuestion', payload);
    },

    // DELETE USER LESSON FROM DB
    deleteUserLesson({state, dispatch, commit}, payload) {
        let class_endpoint = `http://127.0.0.1:8000/api/user_lessons/${payload}/`;
        apiService(class_endpoint, "DELETE")
            .then(data => {
                let id = window.localStorage.getItem('instructor_id');

                // after item is deleted fetch a fresh list of remaining lessons for the logged in user
                dispatch('fetchLessons', id);

                // clears lesson after delete
                commit('clearLessonSelections')
            })
            .catch((err) => {
                console.log(err)
            });
        // commit('deleteUserLesson', payload);
    },


    // POST ACTIONS

    // this action CREATE LESSON DIALOG Post Title to store
    postLessonTitle({commit}, payload) {
        commit('setLessonTitle', payload);
        commit('setIsNew');
    },

    // Posts new lesson to DB after saved
    postLesson({commit, state}) {
        // instructor is being added via serializer from user logged in
        let lesson_endpoint = "http://127.0.0.1:8000/api/user_lessons/";

        // console.log('POST PAYLOAD', state.lesson);
        // var myJSON = JSON.stringify(obj);
        let lessonData = {
            "instructor": {},
            "lesson_title": state.new_lesson_title,
            "lesson_selections": JSON.stringify(state.lesson),
            "class_link": state.new_lesson_class_id,
            "lesson_description": state.new_lesson_description
        };

        // const apiService = function (endpoint, method, data) {
        apiService(lesson_endpoint, "POST", lessonData)
            .then(data => {
                // console.log('results: ', data.results);
                console.log('DATA: ', data);
                // commit('postLesson', data);
                commit('saveLesson', data);
                commit('setLessonID', data);
                commit('seamlessSave')
                                      console.log('SEAMLESSS CALLED1');


            })
            .then(data => {
                commit('setIsEditing');
                commit('clearIsDuplicate');
                commit('clearIsNew');
                  setTimeout(()=>{
                      console.log('SEAMLESSS CALLED2');
                     commit('seamlessSaveOff')
                 }, 3000)


            })
            .catch((err) => {
                console.log(err)
            });


    },

    // PUT action to update lesson in DB after updated
    postLessonUpdate({commit, state}) {

        // instructor is being added via serializer from user logged in
        // let class_endpoint = `http://127.0.0.1:8000/api/class_name/${payload.id}/`;
        let lesson_endpoint = `http://127.0.0.1:8000/api/user_lessons/${state.lesson_id}/`;

        console.log('LESSON TITLE', state.new_lesson_title);
        // var myJSON = JSON.stringify(obj);
        let lessonData = {
            "instructor": {},
            "lesson_title": state.new_lesson_title,
            "lesson_selections": JSON.stringify(state.lesson),
            "class_link": state.new_lesson_class_id,
            "lesson_description": state.new_lesson_description
        };

        // const apiService = function (endpoint, method, data) {
        apiService(lesson_endpoint, "PUT", lessonData)
            .then(data => {
                // console.log('results: ', data.results);
                console.log('DATA: ', data);
                // commit('postLesson', data);
                commit('updateLesson', data);
                 commit('seamlessSave')
            })
             .then(data => {

                 setTimeout(()=>{
                     commit('seamlessSaveOff')
                 }, 3000)

            })
            .catch((err) => {
                console.log(err)
            });
    },


    // STORE DATA ONLY

    // This loads lesson data into lesson store from the data sent from the Dashboard edit btn
    editLesson({commit}, payload) {
        console.log('EDIT PAYLOAD', payload);
        commit('setEditLesson', payload);
    },

    // Clears old lesson store values out when new one is created or once lesson is saved
    clearOldLesson({commit}) {
        commit('clearLessonSelections')
    },

    // like edit lesson but for duplicate sets store values from dashboard duplicate btn
    duplicateLesson({commit}, payload) {
        console.log('EDIT PAYLOAD', payload);
        commit('setDuplicateLesson', payload);
        // commit('setIsDuplicate');
    },

    // This edits lesson  title, description, class only from Review Page edit btn
    editLessonData({commit}, payload) {
        console.log('EDIT PAYLOAD', payload);
        commit('setEditLessonData', payload);
    },

    // clears out editing and bool variable from store
    clearIsEditing({commit}) {
        commit('clearIsEditing');
    }


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
        return state.lesson
    },
    getUserQuestions(state) {
        return state.lesson.user_questions
    },
    getLessons(state) {
        return state.lessons
    },
    getLessonTitle(state) {
        return state.new_lesson_title;
    },
    getClassID(state) {
        return state.new_lesson_class_id;
    },
    getLessonDescription(state) {
        return state.new_lesson_description;
    },
    getLessonID(state) {
        return state.lesson_id;
    },

    getLesson(state) {

        return {
            "lesson_description": state.new_lesson_description,
            "class_link": state.new_lesson_class_id,
            "lesson_title": state.new_lesson_title,
            "lesson_id": state.lesson_id,
            "selections": state.lesson
        };
    },

    getIsEditing(state) {
        return state.is_editing
    },

    getIsDuplicate(state) {
        return state.is_duplicate
    },

    getIsNew(state){
        return state.is_new
    },

    getSeamlessSave(state){
         return state.seamlessSave
    }


};


// export each object
export default {
    state,
    actions,
    mutations,
    getters
}


// http://127.0.0.1:8000/api/user_lessons/c57a93e3-1f84-40eb-8b92-5691292fefc5/
// http://127.0.0.1:8000/api/user_lessons/c57a93e3-1f84-40eb-8b92-5691292fefc5/