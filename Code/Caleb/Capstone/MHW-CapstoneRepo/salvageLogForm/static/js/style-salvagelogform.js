axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

const app = new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data() {
        return {
            vsalvageLogData: {
                Species: '',
                LogDiameter: '24',
                TrunkHeight: '8',
                Address: '',
                Address2: '',
                City: '',
                State: '',
            },
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
            isSubmittedSalvLog: false,
            isSubmitted: false,
            page: 0,
            form_yes: false,
            form_no: false
        }
    },
    methods: {
        submitPost: async function() {
            const response = await axios.post('PersonalContactInfoForm/', this.vuserData)
            console.log(response)
            if (response.status === 200) {
                this.page++
            }
        },
        submitted() {
            this.isSubmitted = true;
            this.submitPost();
        },
        submitSalvLogPost: async function() {
            const response = await axios.post('salvageLogForm/', this.vsalvageLogData)
            console.log(response)
            if (this.vsalvageLogData.LogDiameter < 18) {
                this.form_no = true;
                this.form_yes = false;
                console.log('Log Diameter is too small')
            }
            if (this.vsalvageLogData.TrunkHeight < 6) {
                this.form_no = true;
                this.form_yes = false;
                console.log('Log is too short')
            }
            if (this.vsalvageLogData.LogDiameter > 18) {
                this.form_yes = true;
                this.form_no = false;
                console.log('Log is of a desirable diameter & height')
            }
            if (this.vsalvageLogData.TrunkHeight > 6) {
                this.form_yes = true;
                this.form_no = false;
                console.log('Log is of a desirable height')
            }
            this.page++
        },
        submittedSalvLog() {
            this.isSubmittedSalvLog = true;
            this.submitSalvLogPost();
        },
        EditPersonalInfo() {
            this.page = 0
        },
        EditSalvLogInfo() {
            this.page = 1
        }
    }
})