export const MyFunctions = {

    searchFunction: function (data, search, item) {
        return data.filter(obj => {
            return obj[item].toLowerCase().includes(search.toLowerCase());
        });
    },

    filterSearchFunction: function (data, filter, search, filterItem, searchItem) {


        // if (filter) {

        // create empty array to hold filtered values
        let filteredList = [];

        // loop through each lex item to get to their icon_list
        data.forEach((item) => {

            // loop through each icon list to see if icon matches filter
            item.icon_list.forEach(obj => {

                // if matches add original item to filterList Array
                if (obj[filterItem].toLowerCase() === filter.toLowerCase()) {
                    filteredList.push(item)
                }
            })
        });

        // if there is also a search value and filter value check search against filteredList array
        // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
        if (search.length > 0) {

            // check if items term include search values
            return filteredList.filter(obj => {
                return obj[searchItem].toLowerCase().includes(search.toLowerCase());
            });
        }

        // return filteredList if no search value
        return filteredList


    },

    filterEventsSearch: function(data, filter, search, filterItem, searchItem){

            let filteredList = [];

                    // loop through each lex item to get to their icon_list
                    data.forEach((item) => {

                        // collection_name
                        if (item[filterItem].toLowerCase() === filter.toLowerCase()) {
                            filteredList.push(item)
                        }

                    });

                    // if there is also a search value and filter value check search against filteredList array
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
                    if (search.length > 0) {

                        // check if items term include search values
                        return filteredList.filter(obj => {
                            return obj[searchItem].toLowerCase().includes(search.toLowerCase());
                        });
                        // return filterSearch;
                    }

                    // return filteredList if no search value
                    return filteredList


                }




    // }
};