// import {CSRF_TOKEN} from "./csrf";
import axios from 'axios';
import store from './index'

import {
    Loading,
    // optional!, for example below
    // with custom spinner
    QSpinnerOval
} from 'quasar'
import router from "../router";


// handle the response, if status is 204 meaning no content return
// empty string, else return reponse.json()
function handleResponse(response) {

        console.log("HANDLED CALLED", response);

    //
    // if (response.status === 400) {
    //     Loading.hide();
    //     return 'Sorry Man! Unable to log in with provided credentials.';
    // }
    //
    //
    // if (response.status === 204) {
    //     Loading.hide();
    //     return '';
    // } else if (response.status === 404) {
    //     Loading.hide();
    //     return null;
    // } else {
        // console.log('RESPONSETIME: ', response.data);
        Loading.hide();
        return response.data;
    // }

}

// create a service with config and fetch
// in the config set method or GET
// check if data exist if so stringify the data,
// set headers with csrf

// we are creating a function we can use anywhere
// when we call the function we will pass the endpoint,
// the method and the data if any
const registerService = function (endpoint, method, data) {


    // console.log("METHOD", method);

    // default options
// Loading.show()

// fully customizable
    Loading.show({
        spinner: QSpinnerOval,
        delay: 200,
        // other props
    });


    // set up the config
    // if method not set assume get request
    // if data is supplied stringify it, else set body to null
    // set up header with csrf token and content type
    // console.log('TOKEN: ', CSRF_TOKEN);
    // const config = {
    //     method: method || "GET",
    //     body: data !== undefined ? JSON.stringify(data) : null,
    //     headers: {
    //         "content-type": "application/json",
    //         "X-CSRFTOKEN": CSRF_TOKEN
    //     }
    // };

    // grab the user token from local storage
    // let token = window.localStorage.getItem('access_token');

    const config = {
        method: method || "GET",
        url: endpoint,
        data: data,

    };





        console.log('CONFIG: ', config);


    // set up fetch functon to user config
    // return fetch(endpoint, config)
    //     .then(handleResponse)
    //     .catch(error => console.log(error))


    return axios(config)
        .then(handleResponse)
        .then(() => {
            router.push("/signin");
        })
        .catch((error) => {

            console.log("ERROR INSIDE AXIOS");
            console.log("BIG FAT REGISTRATION ERROR STATUS TEST", error);

            if (error.response.status === 400) {
                // Loading.hide();
                // console.log('NEW NEW NEW Unable to log in with provided credentials.');
                // assign response error to error_message to be displayed on page
                store.commit('error_message', error.response.data)
                // return ;
            }

            if (error.response) {
                console.log('DATA', error.response.data);
                console.log('STATUS', error.response.status);
                console.log('HEADERS', error.response.headers);
            }
            Loading.hide();


    //          if (error.response.status === 400) {
    //     Loading.hide();
    //     return 'Unable to log in with provided credentials.';
    // }



    //         if (error.status === 400) {
    //     Loading.hide();
    //     return 'Unable to log in with provided credentials.';
    // }
    //         console.log('MY DISPLAY', error)
        })



};

export {registerService};