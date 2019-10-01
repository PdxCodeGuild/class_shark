axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

const app = new Vue({
    el: '#salvage-log-form',
    delimiters: ['${', '}'],
    data() {
        return {
            vsalvageLogData: {
                Species: '',
                LogDiameter: '',
                TrunkHeight: '',
                Address: '',
                Address2: '',
                City: '',
                State: '',
            },
            isSubmitted: false
        }
    },
    methods: {
        submitPost: async function() {
            const response = await axios.post('', this.vsalvageLogData)
            console.log(response)
        },
        submitted() {
            this.isSubmitted = true;
            this.submitPost();
        }
    }
})