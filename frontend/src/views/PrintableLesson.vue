<template>

<div>


<!--    NAV-->


            <q-toolbar class="single">

                <q-btn
                        flat
                        dense
                        round
                        @click="backToReview"
                        icon="keyboard_backspace"
                />

                <q-btn flat no-caps no-wrap class="q-ml-xs" v-if="$q.screen.gt.xs">

<!--                    Ideal Icon-->
<!--                    <q-icon dense>-->

<!--                        <svg version="1.1" baseProfile="basic" id="Layer_1"-->
<!--                             xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"-->
<!--                             y="0px" viewBox="0 0 136.75 156.28"-->
<!--                             xml:space="preserve">-->
<!--                            <g>-->
<!--                                <g>-->
<!--                                    <path class="st0"-->
<!--                                          d="M84.73,70.65h50.15c-0.67,46.28-38.36,83.75-84.72,84.05v-50.15C68.87,104.26,84.08,89.28,84.73,70.65z"/>-->
<!--                                    <path class="st0"-->
<!--                                          d="M56.31,40.18V1.42c36.18,0.48,65.65,29.27,67.19,65.19l-38.84,0C83.2,52.08,71.11,40.64,56.31,40.18z"/>-->
<!--                                    <path class="st0" d="M38.1,46.55c-3.77,3.77-6.02,8.65-6.46,13.9H1.78c0.47-13.22,5.83-25.58,15.24-34.98-->
<!--                                        c9.47-9.46,21.92-14.83,35.23-15.24v29.85C46.91,40.46,41.93,42.72,38.1,46.55z"/>-->
<!--                                    <path class="st0"-->
<!--                                          d="M46.11,76.83v21.96C26.85,98.63,11.09,83.53,9.79,64.51h22.08C33.05,71.4,38.96,76.68,46.11,76.83z"/>-->
<!--                                    <path class="st0" d="M56.82,70.65h11.14c-0.47,4.41-2.42,8.5-5.61,11.68c-3.31,3.29-7.59,5.25-12.19,5.62V76.9-->
<!--                                        c1.65-0.31,3.22-1.13,4.45-2.35C55.71,73.46,56.45,72.11,56.82,70.65z"/>-->
<!--                                    <path class="st0" d="M50.97,61.96c-0.31-0.01-0.62,0.02-0.93,0.07v-7.87c0.31-0.02,0.62-0.05,0.93-0.05-->
<!--                                        c3.71,0,7.22,1.46,9.85,4.09c2.28,2.29,3.67,5.23,3.99,8.41h-7.95c-0.26-1.07-0.81-2.07-1.61-2.87-->
<!--                                        C54.11,62.59,52.58,61.96,50.97,61.96z"/>-->
<!--                                </g>-->
<!--                            </g>-->
<!--                            </svg>-->


<!--                    </q-icon>-->

                    <q-toolbar-title shrink class="text-weight-bold">

                    <LogoTemplate/>

                    </q-toolbar-title>
                </q-btn>

                <q-space/>
                <q-space/>

<!--                <TopRightNav/>-->
                 <div style="float: right; text-align: right; width: 20%; display: inline" class="justify-end">
                <q-btn @click="downloadLesson" flat color="gray" label="Download" icon="o_edit"/>
            </div>

            </q-toolbar>



    <!--    <div>TEST TEST TEST</div>-->
<!--        <div class="top-pad title" tabindex="0">-->
<!--            <div style="width: 40%; display: inline">Printable Lesson</div>-->
<!--            <div style="float: right; text-align: right; width: 20%; display: inline" class="justify-end">-->
<!--                <q-btn @click="downloadLesson" flat color="gray" label="Download" icon="o_edit"/>-->
<!--            </div>-->
<!--        </div>-->

    <div class="container-width">




        <div id="LessonLayout">


            <!--            REVIEW CONTAINER-->
            <div class="container" style="width: 100%">

                {{ eventFetch(lesson.selections.selected_event) }}

                <div class="flex-header">
                    <div class="text-h6 single">LESSON OVERVIEW</div>
                </div>


                <!-- ONE-->
                <div class="element_1 inline-block">
                    <div class="columnerInside">

                        <div class="subtitle">Title:</div>
                        <div>{{ lesson.lesson_title }}</div>

                        <div class="subtitle dialog-top ">Description:</div>
                        <div>{{ lesson.lesson_description }}</div>

                        <div class="subtitle dialog-top ">Class:</div>
                        <div>{{ class_card_name(lesson.class_link) }}</div>

                        <div class="subtitle dialog-top ">Grade:</div>
                        <div>{{ class_card_grade(lesson.class_link) }}</div>

                    </div>
                </div>   <!-- end 1 -->


                <!-- TWO-->

                <div class="element_23_container rightColumn inline-block ">

                    <div class="element_2_inner inline-block">
                        <div class="columnerInside">

                            <div class="subtitle ">Event:</div>
                            <div>{{event.event_title}}</div>



                        </div>
                    </div>   <!-- end 2-->


                    <!-- THREE-->
                    <div class="element_3_inner inline-block">

                        <div class="columnerInside rightColumn">

                            <div v-if="reading.title_major" class="subtitle">Primary Focus:</div>
                            <div class="">{{reading.title_major}}</div>

                        </div>

                    </div> <!-- end 3-->

                    <div class="preview-line">
                        <div class="element_2_inner inline-block ">
                            <div class="columnerInside">
                                <div class="subtitle ">Further Explorations:</div>
<!--                                <ol class="">-->
                                    <div v-for="ex in explorationFetch(lesson.selections.selected_exploration)"
                                        :key="ex.id">
                                        {{ex.title_minor}} ({{ex.reading_category.category_name}})
                                    </div>
<!--                                </ol>-->
                            </div>

                        </div>


                        <div class="element_3_inner inline-block">
                            <div class="columnerInside rightColumn">
                                <div class="subtitle ">Questions:</div>

                                <div v-for="question in questionFetch(lesson.selections.selected_questions)"
                                     :key="question.id"> {{question.question}}
                                </div>

                                 <div class="subtitle dialog-top">Teacher Questions:</div>

                                 <div v-for="uquestion in lesson.selections.user_questions"
                                     :key="uquestion.id"> {{uquestion.user_question}}
                                </div>

                            </div>
                        </div>
                    </div>

                    <!--                     <div class="element_2_inner inline-block">-->
                    <div class="columnerInside preview-line">
                        <div class="subtitle ">Lexis:</div>
                        <ol class="lexis-wrapper">
                            <li class="lexis-review" v-for="lex in lexisFetch(lesson.selections.selected_lexis)"
                                :key="lex.id">
                                {{lex.term}}
                            </li>
                        </ol>
                    </div>

                    <!--                       </div>-->


                    <div class="columnerInside preview-line">
                        <div class="subtitle ">Performances:</div>
                        <ol class="excerpt">
                            <li v-for="perf in performanceFetch(lesson.selections.selected_performances)"
                                :key="perf.id"> {{perf.performance_title}}
                            </li>
                        </ol>
                    </div>


                    <div class="columnerInside preview-line">
                        <div class="subtitle ">Extensions:</div>
                        <ol class="excerpt">
                            <li v-html="ext.action"
                                v-for="ext in extensionsFetch(lesson.selections.selected_extensions)"
                                :key="ext.id"></li>
                        </ol>
                    </div>


                </div> <!-- end 23 container-->
            </div> <!-- end container info -->


            <!-- LESSON INFO-->

            <div class="container new-break" style="width: 100%">

                {{ eventFetch(lesson.selections.selected_event) }}

                <!-- ONE-->
                <div class="element_1 inline-block">
                    <div class="columnerInside">

                        <div class="flex-header">
                            <div class="text-h6 single">INFO</div>
                        </div>

                        <div class="subtitle">Title:</div>
                        <div>{{ lesson.lesson_title }}</div>

                        <div class="subtitle dialog-top ">Description:</div>
                        <div>{{ lesson.lesson_description }}</div>

                        <div class="subtitle dialog-top ">Class:</div>
                        <div>{{ class_card_name(lesson.class_link) }}</div>

                        <div class="subtitle dialog-top ">Grade:</div>
                        <div>{{ class_card_grade(lesson.class_link) }}</div>

                    </div>
                </div>   <!-- end 1 -->


                <!-- TWO-->

                <div class="element_23_container rightColumn inline-block">

                    <div class="flex-header">
                        <div class="text-h6 single">EVENT</div>
                    </div>

                    <div class="element_2_inner inline-block">
                        <div class="columnerInside">


                            <div class="subtitle ">Event:</div>
                            <div>{{event.event_title}}</div>

                            <div class="subtitle dialog-top">Descriptor:</div>
                            <div class="excerpt">{{event.event_descriptor}}</div>

                            <div class="subtitle dialog-top ">Collection:</div>
                            <div>{{event.collection_name}}</div>

                        </div>
                    </div>   <!-- end 2-->


                    <!-- THREE-->
                    <div class="element_3_inner inline-block">

                        <div class="columnerInside rightColumn">

                            <div v-if="event.quotation" class="subtitle dialog-top">Quote:</div>
                            <div class="quote">
                                "{{event.quotation}}"
                            </div>
                            <div class="author">
                                – {{event.quotation_author}}
                            </div>
                            <div class="author_source" v-html="event.quote_source">
                            </div>

                        </div>

                    </div> <!-- end 3-->
                </div> <!-- end 23 container-->
            </div> <!-- end container info -->


            <!-- PRIMARY READING-->
            <div class="container" style="width: 100%">
                {{ readingFetch(lesson.selections.selected_reading) }}

                <div class="flex-header">
                    <div class="text-h6 single">PRIMARY READING</div>
                </div>

                <!-- ONE-->
                <div class="element_1 inline-block">
                    <div class="columnerInside">

                        <div v-if="reading.title_major" class="subtitle dialog-top">Title:</div>
                        <div class="">{{reading.title_major}}</div>

                        <div v-if="reading.author_first_name" class="subtitle dialog-top">Author:</div>
                        <div>{{reading.author_first_name}} {{reading.author_last_name}}</div>
                        <div v-if="reading.author_dob" class="subtitle dialog-top">Author DOB:</div>
                        <div>{{reading.author_dob}}</div>


                        <div v-if="reading.level_ability" class="subtitle dialog-top">Reading Level:</div>
                        <div>{{reading.level_ability}}</div>
                        <div v-if="reading.page_count" class="subtitle dialog-top">Page Count:</div>
                        <div>{{reading.page_count}}</div>
                        <div v-if="reading.reading_category.category_name" class="subtitle dialog-top">Type:</div>
                        <div>{{reading.reading_category.category_name}}</div>

                    </div>
                </div>   <!-- end 1 -->


                <!-- TWO-->
                <div class="element_23_container rightColumn inline-block">

                    <div class="columnerInside">
                        <div v-if="reading.synopsis" class="subtitle dialog-top">Synopsis:</div>
                        <div class="excerpt">{{reading.synopsis}}</div>
                    </div>

                </div> <!-- end 23 container-->

            </div> <!-- end container info -->


            <!--            <div class="flex-grid top-pad section-end">-->

            <!--                {{ readingFetch(lesson.selections.selected_reading) }}-->
            <!--                <div class="columner">-->

            <!--                    <div class="flex-header">-->
            <!--                        <div class="text-h6">Primary Focus</div>-->
            <!--                    </div>-->

            <!--                    <div class="flex-grid-twothirds">-->

            <!--                        <div class="columnerInside two">-->


            <!--                            <div v-if="reading.title_major" class="subtitle dialog-top">Title:</div>-->
            <!--                            <div class="">{{reading.title_major}}</div>-->

            <!--                            <div v-if="reading.author_first_name" class="subtitle dialog-top">Author:</div>-->
            <!--                            <div>{{reading.author_first_name}} {{reading.author_last_name}}</div>-->
            <!--                            <div v-if="reading.author_dob" class="subtitle dialog-top">Author DOB:</div>-->
            <!--                            <div>{{reading.author_dob}}</div>-->


            <!--                            <div v-if="reading.level_ability" class="subtitle dialog-top">Reading Level:</div>-->
            <!--                            <div>{{reading.level_ability}}</div>-->
            <!--                            <div v-if="reading.page_count" class="subtitle dialog-top">Page Count:</div>-->
            <!--                            <div>{{reading.page_count}}</div>-->
            <!--                            <div v-if="reading.reading_category.category_name" class="subtitle dialog-top">Type:</div>-->
            <!--                            <div>{{reading.reading_category.category_name}}</div>-->


            <!--                        </div>-->
            <!--                        <div class="columnerInside three">-->

            <!--                            <div v-if="reading.synopsis" class="subtitle dialog-top">Synopsis:</div>-->
            <!--                            <div class="excerpt">{{reading.synopsis}}</div>-->

            <!--                        </div>-->


            <!--                    </div>-->


            <!--                </div>-->

            <!--            </div>-->


            <!--            Further Explorations-->


            <!-- FURTHER READING-->
            <div class="container new-break" style="width: 100%">


                <div class="flex-header">
                    <div class="text-h6">FURTHER EXPLORATIONS</div>

                </div>

                <!-- ONE-->
                <div class="auto-break explorations"
                     v-for="ex in explorationFetch(lesson.selections.selected_exploration)" :key="ex.id">
                    <div class="element_1 inline-block">
                        <div class="columnerInside">


                            <div v-if="ex.title_minor" class="subtitle dialog-top">Title:</div>
                            <div class="">{{ex.title_minor}}</div>

                            <div v-if="ex.author_first_name" class="subtitle dialog-top">Author:</div>
                            <div>{{ex.author_first_name}} {{ex.author_last_name}}</div>
                            <div v-if="ex.author_dob" class="subtitle dialog-top">Author DOB:</div>
                            <div>{{ex.author_dob}}</div>


                            <div v-if="ex.level_ability" class="subtitle dialog-top">Reading Level:</div>
                            <div>{{ex.level_ability}}</div>
                            <div v-if="ex.page_count" class="subtitle dialog-top">Page Count:</div>
                            <div>{{ex.page_count}}</div>
                            <div v-if="ex.reading_category.category_name" class="subtitle dialog-top">Type:</div>
                            <div>{{ex.reading_category.category_name}}</div>

                            <!--                        {{ex.title_minor}}-->

                        </div>
                    </div>   <!-- end 1 -->


                    <!-- TWO-->
                    <div class="element_23_container rightColumn inline-block">

                        <div class="columnerInside">
                            <div v-if="ex.excerpt" class="subtitle dialog-top">Excerpt:</div>
                            <div class="excerpt" v-html="ex.excerpt"></div>

                            <div class="subtitle dialog-top">Resource Link:</div>
                            <div><a :href="ex.resource_link">Download Resource ></a></div>
                        </div>

                    </div> <!-- end 23 container-->
                </div>  <!-- end loop-->

            </div> <!-- end container info -->


            <!--            <div class="flex-grid top-pad section-end ">-->
            <!--                <div class="columner">-->

            <!--                    <div class="flex-header">-->
            <!--                        <div class="text-h6">Further Explorations</div>-->
            <!--                    </div>-->


            <!--                    &lt;!&ndash;this function returns an array that is then looped through&ndash;&gt;-->
            <!--                    <div v-for="ex in explorationFetch(lesson.selections.selected_exploration)" :key="ex.id"-->
            <!--                         class="explorations auto-break">-->

            <!--                        <div class="flex-grid-twothirds">-->

            <!--                            <div class="columnerInside two">-->


            <!--                                <div v-if="ex.title_minor" class="subtitle dialog-top">Title:</div>-->
            <!--                                <div class="">{{ex.title_minor}}</div>-->

            <!--                                <div v-if="ex.author_first_name" class="subtitle dialog-top">Author:</div>-->
            <!--                                <div>{{ex.author_first_name}} {{ex.author_last_name}}</div>-->
            <!--                                <div v-if="ex.author_dob" class="subtitle dialog-top">Author DOB:</div>-->
            <!--                                <div>{{ex.author_dob}}</div>-->


            <!--                                <div v-if="ex.level_ability" class="subtitle dialog-top">Reading Level:</div>-->
            <!--                                <div>{{ex.level_ability}}</div>-->
            <!--                                <div v-if="ex.page_count" class="subtitle dialog-top">Page Count:</div>-->
            <!--                                <div>{{ex.page_count}}</div>-->
            <!--                                <div v-if="ex.reading_category.category_name" class="subtitle dialog-top">Type:</div>-->
            <!--                                <div>{{ex.reading_category.category_name}}</div>-->
            <!--                                &lt;!&ndash;                        {{ex.title_minor}}&ndash;&gt;-->

            <!--                            </div>-->

            <!--                            <div class="columnerInside three">-->
            <!--                                <div v-if="ex.excerpt" class="subtitle dialog-top">Excerpt:</div>-->
            <!--                                <div class="excerpt" v-html="ex.excerpt"></div>-->
            <!--                            </div>-->

            <!--                        </div>-->
            <!--                    </div>-->


            <!--                </div>-->

            <!--            </div>-->


            <!--            Lexis Data-->


            <!-- LEXIS -->
            <div class="container new-break lexis-class text-format" style="width: 100%">

                <div class="flex-header">
                    <div class="text-h6">LEXIS</div>

                </div>

                <div v-for="lex in lexisFetch(lesson.selections.selected_lexis)" :key="lex.id"
                     class="explorations auto-break">


                    <!-- ONE-->
                    <div class="element_1 inline-block">
                        <div class="columnerInside">

                            <div v-if="lex.term" class="subtitle dialog-top">Term:</div>
                            <div class="bolder">{{lex.term}} | {{lex.part_of_speech}}</div>


                            <div v-if="lex.derivations.length > 0" class="subtitle dialog-top">Derivations:</div>
                            <div v-for="der in lex.derivations" :key="der.id">
                                {{der.value}}
                            </div>

                            <div v-if="lex.lexis_root.length > 0" class="subtitle dialog-top">Root:</div>
                            <div v-for="root in lex.lexis_root" :key="root.id">
                                {{root.value}}
                            </div>


                            <div v-if="lex.highlight.length > 0" class="subtitle dialog-top">Highlight:</div>
                            <ul>
                                <li v-for="highlight in lex.highlight" :key="highlight.id">
                                    {{highlight.value}}
                                </li>
                            </ul>

                        </div>
                    </div>   <!-- end 1 -->


                    <!-- TWO-->

                    <div class="element_23_container rightColumn inline-block">
                        <div class="element_2_inner inline-block">
                            <div class="columnerInside">


                                <div v-if="lex.etymology" class="subtitle dialog-top">Etymology:</div>
                                <div class="" v-html="lex.etymology"></div>


                                <div v-if="lex.quotation" class="subtitle dialog-top">Quote:</div>
                                <div class="quote">
                                    "{{lex.quotation}}"
                                </div>
                                <div class="author">
                                    – {{lex.quotation_author}}
                                </div>
                                <div class="author_source" v-html="lex.quote_source">

                                </div>

                            </div>
                        </div>   <!-- end 2-->


                        <!-- THREE-->
                        <div class="element_3_inner top-align inline-block">

                            <div class="columnerInside rightColumn">

                                <div v-if="lex.application.length > 0" class="subtitle dialog-top">Application:</div>
                                <ul>
                                    <li v-for="application in lex.application" :key="application.id">
                                        {{application.value}}
                                    </li>
                                </ul>


                                <div v-if="lex.exploration.length > 0" class="subtitle dialog-top">Exploration:</div>
                                <ol>
                                    <li v-for="exploration in lex.exploration" :key="exploration.id">
                                        {{exploration.value}}
                                    </li>
                                </ol>

                            </div>

                        </div> <!-- end 3-->

                    </div>  <!-- end 2/3 -->

                </div>  <!-- end loop-->
            </div> <!-- end container info -->


            <!--            QUESTIONS-->

            <div class="container new-break" style="width: 100%">

                <div class="flex-header">
                    <div class="text-h6 single">QUESTIONS</div>
                </div>


<!--                <div class="element_50 inline-block columnerInside">-->
                                    <div class="columnerInside">

                    <div v-if="lesson.selections.selected_questions.length > 0"
                         class="subtitle">Key Questions:
                    </div>
                    <div v-for="question in questionFetch(lesson.selections.selected_questions)" :key="question.id"
                         class="auto-break">
                        {{question.question}}
                    </div>

                    <div v-if="lesson.selections.user_questions.length > 0"
                         class="subtitle dialog-top">Teacher Questions:
                    </div>
                    <div v-for="question in lesson.selections.user_questions" :key="question.id"
                         class="auto-break">
                        {{question.user_question}}
                    </div>
                </div>

<!--                                <div class="element_50 inline-block columnerInside rightColumn">-->

<!--                <div class=" inline-block columnerInside rightColumn">-->
<!--                    <div v-if="lesson.selections.user_questions.length > 0"-->
<!--                         class="subtitle dialog-top">Teacher Questions:-->
<!--                    </div>-->
<!--                    <div v-for="question in lesson.selections.user_questions" :key="question.id"-->
<!--                         class="auto-break">-->
<!--                        {{question.user_question}}-->
<!--                    </div>-->
<!--                </div>-->


            </div>


            <!--            <div class="flex-grid top-pad section-end  lexis-class">-->
            <!--                <div class="columner">-->

            <!--                    <div class="flex-header">-->
            <!--                        <div class="text-h6">Lexis</div>-->
            <!--                    </div>-->

            <!--                    <div v-for="lex in lexisFetch(lesson.selections.selected_lexis)" :key="lex.id"-->
            <!--                         class="explorations auto-break">-->

            <!--                        <div class="flex-grid-thirds">-->


            <!--                            <div class="columner-1">-->

            <!--                                <div v-if="lex.term" class="subtitle dialog-top">Term:</div>-->
            <!--                                <div class="">{{lex.term}} | {{lex.part_of_speech}}</div>-->


            <!--                                <div v-if="lex.derivations.length > 0" class="subtitle dialog-top">Derivations:</div>-->
            <!--                                <div v-for="der in lex.derivations" :key="der.id">-->
            <!--                                    {{der.value}}-->
            <!--                                </div>-->

            <!--                                <div v-if="lex.lexis_root.length > 0" class="subtitle dialog-top">Root:</div>-->
            <!--                                <div v-for="root in lex.lexis_root" :key="root.id">-->
            <!--                                    {{root.value}}-->
            <!--                                </div>-->


            <!--                                <div v-if="lex.highlight.length > 0" class="subtitle dialog-top">Highlight:</div>-->
            <!--                                <ul>-->
            <!--                                    <li v-for="highlight in lex.highlight" :key="highlight.id">-->
            <!--                                        {{highlight.value}}-->
            <!--                                    </li>-->
            <!--                                </ul>-->


            <!--                            </div>-->

            <!--                            <div class="columner-2">-->

            <!--                                <div v-if="lex.etymology" class="subtitle dialog-top">Etymology:</div>-->
            <!--                                <div class="excerpt" v-html="lex.etymology"></div>-->


            <!--                                <div class="dialog-top quote">-->
            <!--                                    "{{lex.quotation}}"-->
            <!--                                </div>-->
            <!--                                <div class="author">-->
            <!--                                    – {{lex.quotation_author}}-->
            <!--                                </div>-->
            <!--                                <div class="author_source" v-html="lex.quote_source">-->

            <!--                                </div>-->


            <!--                            </div>-->


            <!--                            <div class="columner-3">-->

            <!--                                <div v-if="lex.application.length > 0" class="subtitle dialog-top">Application:</div>-->
            <!--                                <ul>-->
            <!--                                    <li v-for="application in lex.application" :key="application.id">-->
            <!--                                        {{application.value}}-->
            <!--                                    </li>-->
            <!--                                </ul>-->


            <!--                                <div v-if="lex.exploration.length > 0" class="subtitle dialog-top">Exploration:</div>-->
            <!--                                <ol>-->
            <!--                                    <li v-for="exploration in lex.exploration" :key="exploration.id">-->
            <!--                                        {{exploration.value}}-->
            <!--                                    </li>-->
            <!--                                </ol>-->


            <!--                            </div>-->
            <!--                        </div>-->

            <!--                    </div>-->
            <!--                </div>-->
            <!--            </div>-->


            <!--            Performances-->

            <div class="container new-break lexis-class text-format" style="width: 100%">

                <div class="flex-header">
                    <div class="text-h6">PERFORMANCES</div>

                </div>

                <div v-for="perf in performanceFetch(lesson.selections.selected_performances)" :key="perf.id"
                     class="explorations auto-break">

                    <!-- ONE-->
                    <div class="element_1 inline-block">
                        <div class="columnerInside">

                            <div v-if="perf.performance_title" class="subtitle dialog-top">Title:</div>
                            <div class="bolder"> {{perf.performance_title}}</div>

                            <div class="subtitle dialog-top">Resource Link:</div>
                            <div class=""><a :href="perf.resource_link">Download Resource ></a></div>


                            <div class="subtitle dialog-top">Sample Link:</div>
                            <div class=""><a :href="perf.student_sample">Download Sample ></a></div>

                            <div class="subtitle dialog-top">Video Link:</div>
                            <div class=""><a href="http://google.com">Download Video ></a></div>


                        </div>
                    </div>   <!-- end 1 -->


                    <!-- TWO-->

                    <div class="element_23_container rightColumn inline-block">
                        <div class="element_2_inner inline-block">
                            <div class="columnerInside">


                                <div v-if="perf.performance_description" class="subtitle dialog-top">Description:</div>
                                <div class="">{{perf.performance_description}}</div>

                                <div v-if="perf.performance_overview" class="subtitle dialog-top">Overview:</div>
                                <div class="" v-html="perf.performance_overview"></div>

                            </div>
                        </div>   <!-- end 2-->


                        <!-- THREE-->
                        <div class="element_3_inner top-align inline-block">

                            <div class="columnerInside rightColumn">

                                <div v-if="perf.performance_feat_link.length > 0" class="subtitle dialog-top">Feats:
                                </div>
                                <ul>
                                    <li v-for="feat in perf.performance_feat_link" :key="feat.id">
                                        {{feat.performance_feats}}
                                    </li>
                                </ul>


                            </div>

                        </div> <!-- end 3-->

                    </div>  <!-- end 2/3 -->

                </div>  <!-- end loop-->
            </div> <!-- end container info -->


            <!--            extensions-->

            <div class="container new-break lexis-class text-format" style="width: 100%">

                <div class="flex-header">
                    <div class="text-h6">EXTENSIONS</div>

                </div>

                <div v-for="ext in extensionsFetch(lesson.selections.selected_extensions)" :key="ext.id"
                     class="explorations auto-break">

                    <!-- ONE-->
                    <div class="element_1 inline-block">
                        <div class="columnerInside">

                            <div v-if="ext.action" class="subtitle dialog-top">Action:</div>
                            <div class="bolder" v-html="ext.action"></div>

                            <div v-if="ext.assignment_command_types.command_name" class="subtitle dialog-top">Command:
                            </div>
                            <div class="">{{ext.assignment_command_types.command_name}}</div>


                            <div class="subtitle dialog-top">Video Link:</div>
                            <div class=""><a :href="ext.video_link">Watch Video ></a></div>


                        </div>
                    </div>   <!-- end 1 -->


                    <!-- TWO-->

                    <div class="element_23_container rightColumn inline-block">

                        <div class="columnerInside">
                            <div v-if="ext.explanation" class="subtitle dialog-top">Explanation:</div>
                            <div class="excerpt" v-html="ext.explanation"></div>
                        </div>

                    </div> <!-- end 23 container-->

                </div>  <!-- end loop-->
            </div> <!-- end container info -->


            <!--            GOALS-->

            <div class="container new-break lexis-class text-format" style="width: 100%">

                <div class="flex-header">
                    <div class="text-h6">GOALS</div>

                </div>

                <div v-for="goal in goalsFetch(lesson.selections.selected_goals)" :key="goal.id"
                     class="explorations auto-break">

                    <!-- ONE-->
                    <div class="element_1 inline-block">
                        <div class="columnerInside">

                            <div v-if="goal.goal" class="subtitle dialog-top">Goal:</div>
                            <div class="bolder" v-html="goal.goal"></div>

                            <div v-if="goal.standard_type" class="subtitle dialog-top">Standard Category:</div>
                            <div class="" v-html="goal.standard_type.standard_type"></div>


                            <div class="subtitle dialog-top">Video Link:</div>
                            <div class=""><a :href="goal.video_link">Watch Video ></a></div>


                        </div>
                    </div>   <!-- end 1 -->


                    <!-- TWO-->

                    <div class="element_23_container rightColumn inline-block">

                        <div class="columnerInside">
                            <div v-if="goal.explanation" class="subtitle dialog-top">Explanation:</div>
                            <div class="excerpt" v-html="goal.explanation"></div>
                        </div>

                    </div> <!-- end 23 container-->

                </div>  <!-- end loop-->
            </div> <!-- end container info -->


        </div>
        <!--        end lesson layout-->


        <!--        CSS-->
        <!--        RD4	7.7 x 10.7 in	196 x 273 mm-->
        <div id="css" v-show="false">


            * {
            margin: 0;
            padding: 0;
            }

            a{
            color: black;
            text-decoration: underline;
            }

            html {
            font-family: Roboto, Arial, serif;
            font-weight: normal;
            font-size: 9pt;
            -moz-hyphens: auto;
            -ms-hyphens: auto;
            -webkit-hyphens: auto;
            hyphens: auto;
            counter-reset: footnote;

            <!--            text-align: justify;-->

            }

            h1 {
            font-weight: bold;
            font-size: 20pt;
            text-indent: 0;

            break-after: avoid;
            }

            h1 + figure {
            margin-bottom: 8pt;
            }

            h2 {
            font-weight: bold;
            font-size: 12pt;
            text-indent: 0;

            break-after: avoid;
            }

            p + p {
            text-indent: 1.5em;
            }

            figure {
            text-align: center;
            }

            img {
            max-width: 100%;
            max-height: 4in;
            }

            figcaption {
            font-size: 9pt;
            }

            .page-top-float {
            margin-bottom: 8pt;
            }

            @page {
            size: 196mm 273mm;
            margin: 20mm 10mm;
            @bottom-center {
            content: counter(page);
            }
            @top-center {
            content: env(doc-title);
            }
            }
            .footnote {
            float: footnote;
            font-size: 8pt;
            counter-increment: footnote;
            text-indent: 0;
            }

            .footnote::footnote-marker {
            content: counter(footnote);
            font-size: 8pt;
            vertical-align: super;
            }

            .footnote::footnote-call {
            content: counter(footnote);
            font-size: 8pt;
            vertical-align: super;
            display: inline;
            line-height: 1;
            }


            <!--             PAGE SPECIFIC-->


            .flex-grid {
            <!--            display: flex;-->
            }

            /*.flex-grid-twos {*/
            /* display: flex;*/
            /* justify-content: space-between;*/
            /*}*/

            .flex-grid-thirds, .flex-grid-twos, .flex-grid-twothirds {
            <!--            display: flex;-->
            justify-content: space-between;
            }


            .flex-grid .columner {
            flex: 1;
            }

            .flex-grid-thirds .columner {
            width: 32%;
            }

            .flex-grid-twothirds .two {
            width: 25%;
            }

            .flex-grid-twothirds .three {
            width: 74%;
            }

            .flex-grid-twos .columner {
            width: 49%;
            }


            * {
            box-sizing: border-box;
            }

            .top-pad {
            padding-top: 20px;
            }

            .dialog-top {
            padding-top: 10px;
            }

            body {
            padding: 20px;
            line-height: 1.35;

            }

            .flex-grid {
            margin: 0 0 0 0;
            }

            .columner {
            <!--            padding: 20px;-->
            <!--            border: 1px solid #cccccc;-->
            }

            .columnerInside {
            <!--             padding: 20px;-->

            }

            /*1063 x 1375 */
            .container-width {
            width: 1063px;
            margin: auto;
            }


            /*titles*/


            .subtitle {
            font-size: 10px;
            color: gray;
            font-weight: normal;
            /*border-bottom: 1px solid gray;*/
            }

            .rightColumn{
            padding-left: 20px;
            }


            .quote {
            font-size: 1rem;
            line-height: 1.35rem;
            font-family: "Times New Roman", serif;
            }

            .author {
            text-align: right;
            font-size: .8rem;
            padding-top: 10px;
            }

            .author_source {
            <!--            padding-top: 10px; -->
            font-size: 10px;
            width: 75%;
            float: right;
            text-align: right;
            line-height: 1;
            }

            .new-break {
            page-break-before: always;
            }

            .auto-break {

            display: block;
            page-break-inside: avoid;

            <!--            page-break-before: auto;-->
            }


            .excerpt{
            text-align: justify;
            line-height: 1.35rem;
            }


            .explorations{
            padding-bottom: 20px;
            border-top: 1px solid #ccc;
            }

            .text-h6{
            margin-top:0px;
            <!--        margin-bottom: 10px;-->
            font-weight: bold;
            padding-bottom: 5px;

            <!--        border-bottom: 1px solid #ccc;-->

            }

            .single{

            border-bottom: 1px solid #ccc;
            margin-bottom: 10px;

            }

            .section-end{

            }

            .two{
            padding-right: 20px
            }


            <!--            lexis-->

            .flex-grid-thirds .columner-1 {
            width: 25%;

            }

            .flex-grid-thirds .columner-2 {
            width: 40%;
            padding-right: 20px;

            }

            .flex-grid-thirds .columner-3 {
            width: 34%;

            }

            .lexis-class ul, ol{
            padding-left: 15px;
            margin: 0;
            }


            <!--            this is non flex styles-->

            .container {

            display: block;
            vertical-align: top;
            padding-top: 40px;
            }

            .element {
            padding: 0.5em;
            background-color: rgba(21, 101, 192, 1);
            color: rgba(255, 255, 255, 1);
            }

            .element_1 {
            width: 24%;
            vertical-align: top;
            }

            .element_2 {
            width: 34%;
            vertical-align: top;
            }

            .element_3 {
            width: 40%;
            vertical-align: bottom;
            }

            .element_50 {
            width: 49.5%;
            vertical-align: top;
            }

            .inline-block {
            display: inline-block;
            }

            .title{
            width: 100%
            }

            .element_23_container{
            width: 75%;
            }

            .element_2_inner {
            width: 45%;
            vertical-align: top;
            }

            .element_3_inner {
            width: 54%;
            vertical-align: top;
            }

            .bolder{
            font-weight: bold;
            }

            .lexis-author {
            text-align: left;
            font-size: .8rem;
            padding-top: 10px;
            }

            .top-align{
            vertical-align: top !important;
            }

            .text-format {
            line-height: 1.35rem;
            }

            .lexis_author_source {
            padding-top: 0px;
            font-size: 10px;
            }


            .lexis-review {
            width: 24%;
            display: inline-block;


            }

            .lexis-wrapper {
            padding: 0;
            margin: 0;

            }

            .preview-line{

            padding-top: 15px;
            margin-top: 15px;
            border-top: 1px solid #ccc;

            }

            .preview-left{
            border-left: 1px solid #ccc;
            }


        </div>



    </div>

    </div>

</template>

<script>
    import {printHTML} from "@vivliostyle/print";
    // import TopRightNav from "@/components/TopRightNav.vue";
    import LogoTemplate from "../components/LogoTemplate";

    export default {
        name: "PrintableLesson.vue",

        data() {
            return {
                event: '',
                reading: '',
                explorations: [],
            }
        },

         components: {

            LogoTemplate
        },

        computed: {
            lesson() {
                return this.$store.getters["getLesson"];
            }
        },

        methods: {

            backToReview(){
                this.$router.back();
            },

            class_card_name(id) {
                console.log('CARD ID', id);
                let classes = this.$store.getters["getUserClasses"];
                let classObj = classes.find(element => element.id === id);
                if (classObj) {
                    return classObj.class_name;
                } else {
                    return;
                }
            },

            class_card_grade(id) {
                let classes = this.$store.getters["getUserClasses"];
                let classObj = classes.find(element => element.id === id);
                if (classObj) {
                    return classObj.grade_level;
                } else {
                    return;
                }
            },

            eventFetch(id) {
                let events = this.$store.getters["getEvents"];
                let eventObj = events.find(element => element.id === id);
                if (eventObj) {
                    this.event = eventObj;
                    // return eventObj.event_title;
                }
            },

            readingFetch(id) {
                let readings = this.$store.getters["getReadings"];
                let readingObj = readings.find(element => element.id === id);
                if (readingObj) {
                    this.reading = readingObj;
                    // return eventObj.event_title;
                }
            },

            explorationFetch(arr) {


                console.log("EXPLORATIONFETCH CALLED");

                // fetch Explorations
                let explorations = this.$store.getters["getExplorations"];
                // console.log("EXPLORATIONS",explorations);


                // fitler explorations against array index ~ return only what matches
                // arr.indexOf(item.id) === -1 return what doesn't match'

                // let explorationArray = explorations.filter(function (item) {
                //     console.log("ITEM",item);
                //     return ~arr.indexOf(item.id);
                // });


                return explorations.filter(function (item) {
                    console.log("ITEM", item);
                    return ~arr.indexOf(item.id);
                });
                // let explorationArray = []


                // console.log('EXPLORATIONARRAY', explorationArray);
                // assign filtered array to explorations
                // this.explorations = explorationArray;

            },


            lexisFetch(arr) {


                console.log("LexisFETCH CALLED", arr);

                // fetch all lexis terms
                let lexis = this.$store.getters["getLexis"];

                return lexis.filter(function (item) {
                    console.log("ITEM", ~arr.indexOf(item.id));
                    return ~arr.indexOf(item.id);
                });

            },

            questionFetch(arr) {

                let questions = this.$store.getters["getQuestions"];

                return questions.filter(function (item) {
                    console.log("ITEM", ~arr.indexOf(item.id));
                    return ~arr.indexOf(item.id);
                });

            },

            performanceFetch(arr) {

                let performances = this.$store.getters["getPerformances"];

                return performances.filter(function (item) {
                    console.log("ITEM", ~arr.indexOf(item.id));
                    return ~arr.indexOf(item.id);
                });

            },

            extensionsFetch(arr) {

                let extensions = this.$store.getters["getExtensions"];

                return extensions.filter(function (item) {
                    console.log("ITEM", ~arr.indexOf(item.id));
                    return ~arr.indexOf(item.id);
                });

            },

            goalsFetch(arr) {

                let goals = this.$store.getters["getGoals"];

                return goals.filter(function (item) {
                    console.log("ITEM", ~arr.indexOf(item.id));
                    return ~arr.indexOf(item.id);
                });

            },


            downloadLesson() {


                var config = {
                    title: 'Ideal Education',
                    printCallback: iframeWin => iframeWin.print() // optional: only needed if calling something other than window.print() for printing.
                };

                // const temp = document;
                // var myobj = temp.getElementsByClassName("q-drawer-container")[0];
                // myobj.remove();

                const content = document.getElementById("LessonLayout").innerHTML;

                // const content = this.$refs.foo.$el.innerHTML;

                // const t = document.getElementById("html").value;
                const e = document.getElementById("css").innerText;

                console.log('STYLES', e);

                // n = document.getElementById("title").value;


                const template = `\n  <!doctype html>\n <html>\n <head>\n <title>${config.title}</title>\n  <style>${e}</style>\n  <head>\n  <body>${content}</body>\n </html>`;
                // const children = this.$refs.foo.$el.children;
                //
                // const styles = this.$refs.foo.$el;
                // const full = this.$refs.foo;
                //
                // console.log('HTML', template);
                // console.log('children', children);
                //
                // console.log('STYLES', styles);
                //                 console.log('FULL', full);


                //
                //        const t = document.getElementById("html").value,
                // e = document.getElementById("css").value,
                // n = document.getElementById("title").value;
                // `\n  <!doctype html>\n <html>\n <head>\n <title>${n}</title>\n  <style>${e}</style>\n  <head>\n  <body>${t}</body>\n </html>`
                // const template =  document.documentElement.outerHTML;
                // const template =  document.getElementById("main-lesson-review");
                // var myobj = template.getElementsByClassName("q-drawer-container");
                // myobj.remove();
//
//                 var myobj = document.getElementById("demo");
// myobj.remove();
                console.log('HTML RENDER', template);
                printHTML(template, config);
                console.log('DOWNLOAD CLICKED')
            },


        }
    }
</script>

<style scoped>


    /*.printRow {*/
    /*    display: flex;*/
    /*    flex-direction: row;*/
    /*    flex-wrap: wrap;*/
    /*}*/

    /*.printColumn {*/
    /*    flex-basis: 100%;*/
    /*    */
    /*}*/

    /*@media screen and (min-width: 800px) {*/
    /*    .printColumn {*/
    /*        flex: 1;*/
    /*    }*/
    /*}*/


    .flex-grid {
        display: flex;
    }

    /*.flex-grid-twos {*/
    /*    display: flex;*/
    /*    justify-content: space-between;*/
    /*}*/

    .flex-grid-thirds, .flex-grid-twos, .flex-grid-twothirds {
        display: flex;
        justify-content: space-between;
    }


    .flex-grid .columner {
        flex: 1;
    }

    .flex-grid-thirds .columner {
        /*width: 32%;*/


    }

    .flex-grid-thirds .columner-1 {
        width: 25%;

    }

    .flex-grid-thirds .columner-2 {
        width: 40%;
        padding-right: 20px;

    }

    .flex-grid-thirds .columner-3 {
        width: 34%;

    }

    .flex-grid-twothirds .two {
        width: 25%;
    }

    .flex-grid-twothirds .three {
        width: 74%;
    }

    .flex-grid-twos .columner {
        width: 49%;
    }


    * {
        box-sizing: border-box;
    }

    .top-pad {
        padding: 20px;
        background-color: #ccc;
    }

    body {
        padding: 20px;
        line-height: 1.35;

    }

    .flex-grid {
        margin: 0 0 0 0;
    }

    .columner {
        /*background: lightgray;*/
        /*padding: 20px;*/
    }

    .columnerInside {
        /*padding: 20px;*/
    }

    /*1063 x 1375  */
    .container-width {
        width: 1063px;
        margin: auto;
    }


    /*titles*/

    .title {

    }

    .subtitle {
        color: gray;
        font-weight: normal;
        /*border-bottom: 1px solid gray;*/
    }

    .rightColumn {
        padding-left: 20px;
    }


    .quote {
        font-size: 1rem;
        line-height: 1.35rem;
        font-family: "Times New Roman", serif;
    }

    .author {
        text-align: right;
        font-size: .8rem;
        padding-top: 10px;
    }

    .author_source {
        /*padding-top: 10px;*/
        font-size: 10px;
        width: 75%;
        float: right;
        text-align: right;
        line-height: 1;
    }

    .excerpt {
        text-align: justify;
        line-height: 1.35rem;
    }

    .explorations {
        padding-bottom: 20px;
        border-top: 1px solid #ccc;
    }

    .text-h6 {
        margin-top: 0px;
        /*margin-bottom: 10px;*/
        font-weight: bold;
        padding-bottom: 5px;
        /*border-bottom: 1px solid #ccc;*/
    }

    .section-end {
        border-bottom: 1px solid #ccc;
    }

    .two {
        padding-right: 20px;
    }

    .lexis-class ul, ol {
        padding-left: 15px;
        margin: 0;
    }


    .container {
        /*padding: 0.5em;*/
        /*background-color: rgba(255, 255, 255, 1);*/
        /*box-shadow: 0px 2px 3px 0px rgba(0, 0, 0, 0.1);*/
        display: block;
        /*margin-bottom: 1em;*/
        padding-top: 40px;

    }

    .element {
        /*padding: 0.5em;*/
        /*background-color: rgba(21, 101, 192, 1);*/
        /*color: rgba(255, 255, 255, 1);*/
    }

    .element_1 {
        width: 24%;
        vertical-align: top;
        /*background-color: rgba(21, 101, 192, 1);*/
        /*color: rgba(255, 255, 255, 1);*/
    }

    .element_2 {
        width: 35%;
        vertical-align: top;

        /*background-color: rgba(21, 101, 192, 1);*/
        /*color: rgba(255, 255, 255, 1);*/
    }

    .element_3 {
        width: 40%;
        vertical-align: bottom;

        /*background-color: rgba(21, 101, 192, 1);*/
        /*color: rgba(255, 255, 255, 1);*/
    }

    .element_23_container {
        width: 75%;
    }

    .element_2_inner {
        width: 45%;
        vertical-align: top;
    }

    .element_3_inner {
        width: 54%;
        vertical-align: top;
    }

    .inline-block {
        display: inline-block;
    }

    .bolder {
        font-weight: bold;
    }

    .lexis-author {
        text-align: left;
        font-size: .8rem;
        padding-top: 10px;
    }

    .top-align {
        vertical-align: top !important;
    }


    .text-format {
        line-height: 1.35rem;
    }

    .lexis_author_source {
        padding-top: 0px;
        font-size: 10px;
    }

    .element_50 {
        width: 49.5%;
        vertical-align: top;
    }

    a {
        color: black;
        text-decoration: underline;
    }

    .single {

        border-bottom: 1px solid #ccc;
        margin-bottom: 10px;
    }


    .lexis-review {
        width: 24%;
        display: inline-block;


    }

    .lexis-wrapper {
        padding: 0;
        margin: 0;

    }

    .preview-line {

        padding-top: 15px;
        margin-top: 15px;
        border-top: 1px solid #ccc;

    }

    .preview-left {
        border-left: 1px solid #ccc;
    }


</style>


<!--//HTML-->
<!--<div class="container">-->
<!--  <div class="element inline-block">Element 1</div>-->
<!--  <div class="element inline-block">Element 2</div>-->
<!--  <div class="element inline-block">Element 3</div>-->
<!--</div>-->
<!--//CSS-->
<!--.container {-->
<!--  padding: 0.5em;-->
<!--  background-color: rgba(255, 255, 255, 1);-->
<!--  box-shadow: 0px 2px 3px 0px rgba(0, 0, 0, 0.1);-->
<!--  display: block;-->
<!--  margin-bottom: 1em;-->
<!--}-->
<!--.element {-->
<!--  padding: 0.5em;-->
<!--  background-color: rgba(21, 101, 192, 1);-->
<!--  color: rgba(255, 255, 255, 1);-->
<!--}-->
<!--.inline-block {-->
<!--  display: inline-block;-->
<!--}-->
