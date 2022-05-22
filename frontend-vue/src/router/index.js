import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/solve',
      name: 'solve',
      component: () => import('../views/Solve.vue'),
    },
    {
      path: '/categories/',
      name: 'categories',
      component: () => import('../views/Categories.vue'),
      children: [
        { path: '/categories/view', name:'/categories/view', component: () => import('../components/ViewCategory.vue')}
      ]
    }
  ]
})

export default router
