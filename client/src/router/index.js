import Vue from 'vue'
import VueRouter from 'vue-router'
import Auth from '../views/Login.vue'
import Home from '../views/Home.vue'
import UsersData from '../views/UsersData.vue'
import APIData from '../views/APIData.vue'
import ReviewsData from '../views/ReviewsData.vue'
import NotFound from '../views/page404.vue'
import ReportReviews from '../views/ReportReviews.vue'
import CompareReviews from '../views/CompareReviews.vue'
import SupportUser from '../views/SupportUser.vue'
import QAUsers from '../views/QAUsers.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/signin',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/users',
    name: 'UsersData',
    component: UsersData
  },
  {
    path: '/apiconfig',
    name: 'APIConfig',
    component: APIData
  },
  {
    path: '/supportusers',
    name: 'SupportUser',
    component: SupportUser
  },
  {
    path: '/reviews',
    name: 'ReviewsData',
    component: ReviewsData
  },
  {
    path: '/reportreviews',
    name: 'ReportReviews',
    component: ReportReviews
  },
  {
    path: '/comparereviews',
    name: 'CompareReviews',
    component: CompareReviews
  },
  {
    path: '/faqusers',
    name: 'QAUsers',
    component: QAUsers
  },
  {
    path: '/404',
    name: '404',
    component: NotFound
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
