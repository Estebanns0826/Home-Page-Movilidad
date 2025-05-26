// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: '2024-11-01',
    devtools: {enabled: true},
    css: ['bootstrap/dist/css/bootstrap.min.css'],

    vite: {
        define: {
            'process.env.DEBUG': false,
        },
    },

    modules: ['@vesp/nuxt-fontawesome'],
    fontawesome: {
        component: 'fa',
        suffix: true,
        icons: {
            solid: ['cog', 'envelope'],
        },
    }
})
