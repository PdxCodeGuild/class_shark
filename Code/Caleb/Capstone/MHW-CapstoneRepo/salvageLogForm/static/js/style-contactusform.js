axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

const app = new Vue({
    el: '#log-form',
    delimiters: ['{$', '$}'],
    data() {
        return {
            vuserData: {
                Name: '',
                Email: '',
                Address: '',
                Address2: '',
                City: '',
                State: '',
                SalvageLogInquiryCheck: true,
                MillingKilnInquiryCheck: true,
                LumberyardInquiryCheck: true,
            },
            isSubmitted: false
        }
    },
    methods: {
        submitPost: async function() {
            const response = await axios.post('', this.vuserData)
            console.log(response)
        },
        submitted() {
            this.isSubmitted = true;
            this.submitPost();
        }
    }
})