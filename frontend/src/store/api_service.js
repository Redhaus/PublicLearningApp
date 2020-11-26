// import {CSRF_TOKEN} from "./csrf";
import axios from 'axios';

import {
    Loading,
    // optional!, for example below
    // with custom spinner
    QSpinnerOval
} from 'quasar'


// handle the response, if status is 204 meaning no content return
// empty string, else return reponse.json()
function handleResponse(response) {

    console.log('HANDLE LOAD HIDE CALLED');

    Loading.hide();
    if (response.status === 204) {
        // Loading.hide();
        return '';
    } else if (response.status === 404) {
        // Loading.hide();
        return null;
    } else if (response.status === 400) {
        // Loading.hide();
        // return null;
    } else {
        // console.log('RESPONSETIME: ', response.data);
        // Loading.hide();
        return response.data;
    }

}

// create a service with config and fetch
// in the config set method or GET
// check if data exist if so stringify the data,
// set headers with csrf

// we are creating a function we can use anywhere
// when we call the function we will pass the endpoint,
// the method and the data if any
const apiService = function (endpoint, method, data) {


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
    let token = window.localStorage.getItem('access_token');

    const config = {
        method: method || "GET",
        url: endpoint,
        data: data,
        headers: {
            "content-type": "application/json",
            // "X-CSRFTOKEN": CSRF_TOKEN,
            "Authorization": "Token " + token
        }
    };



        // console.log('CONFIG: ', config);


    // set up fetch functon to user config
    // return fetch(endpoint, config)
    //     .then(handleResponse)
    //     .catch(error => console.log(error))


    return axios(config)
        .then(handleResponse)
        // .catch((error, msg) => {
        //
        //     console.log('AXIOS MSG', msg);
        //     console.log('AXIOS RESPONSE', error.response);
        //     console.log('DATA', error.response.data[0]);
        //
        //     // console.log('AXIOS RESPONSE', error.response.data.message);
        //     console.log('AXIOS ERROR', error)
        //
        // }
        // )



};

export {apiService};