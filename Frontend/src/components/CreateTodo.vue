<template>
  <v-app style="padding: 10px;">
    <form>
      <v-text-field
        v-model="title"
        :error-messages="titleErrors"
        :counter="45"
        label="Title"
        required
        @input="$v.title.$touch()"
        @blur="$v.title.$touch()"
      ></v-text-field>
      <!--
      <v-text-field
        v-model="email"
        :error-messages="emailErrors"
        label="E-mail"
        required
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
      ></v-text-field>
      -->
      <v-textarea
        v-model="content"
        :error-messages="contentErrors"
        auto-grow
        box
        color="deep-purple"
        label="Content"
        required
        @input="$v.content.$touch()"
        @blur="$v.content.$touch()"
        rows="5"
      ></v-textarea>
      <v-select
        v-model="priority"
        :items="priorities"
        item-text="text"
        item-value="value"
        :error-messages="priorityErrors"
        label="Priority"
        required
        @change="$v.priority.$touch()"
        @blur="$v.priority.$touch()"
      ></v-select>
      <v-checkbox
        v-model="deadineYN"
        label="Insert deadline"
        @change="$v.deadineYN.$touch()"
        @blur="$v.deadineYN.$touch()"
      ></v-checkbox>
      <div v-if="deadineYN">
        <date-picker v-model="deadline" :config="options"></date-picker>
      </div>
      <div style="margin-top: 10px">
        <v-btn color="primary" @click="submit">submit</v-btn>
        <v-btn @click="clear">clear</v-btn>
      </div>
    </form>
  </v-app>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'
   
  export default {
    mixins: [validationMixin],
    validations: {
      title: { required, maxLength: maxLength(45) },
      content: { required },
    //   email: { required, email },
      priority: { required },
      deadineYN: {
        checked (val) {
          return val
        }
      }
    },
    data: () => ({
      title: '',
    //   email: '',
      content: '',
      priority: null,
      priorities: [
        { text: '중요', value: 0 },
        { text: '보통', value: 1 },
        { text: '사소', value: 2 }
      ],
      deadineYN: false,
      deadline: new Date(),
      options: {
        // format: 'YYYY-MM-DD HH:mm',
        useCurrent: false,
      }  
    }),
    computed: {
      priorityErrors () {
        const errors = []
        if (!this.$v.priority.$dirty) return errors
        !this.$v.priority.required && errors.push('Priority is required')
        return errors
      },
      titleErrors () {
        const errors = []
        if (!this.$v.title.$dirty) return errors
        !this.$v.title.maxLength && errors.push('Title must be at most 45 characters long')
        !this.$v.title.required && errors.push('Title is required.')
        return errors
      },
      contentErrors () {
        const errors = []
        if (!this.$v.content.$dirty) return errors
        !this.$v.content.required && errors.push('Content is required.')
        return errors
      }
    //   emailErrors () {
    //     const errors = []
    //     if (!this.$v.email.$dirty) return errors
    //     !this.$v.email.email && errors.push('Must be valid e-mail')
    //     !this.$v.email.required && errors.push('E-mail is required')
    //     return errors
    //   }
    },
    methods: {
      submit () {
        this.$v.$touch()
        if (this.title && this.content && this.priority !== null) {
            console.log(this.title, this.content, this.priority, this.deadineYN, this.deadline)
            var payload = {
              title: this.title,
              content: this.content,
              priority: this.priority,
              deadline: this.deadineYN ? this.$moment(this.deadline).format('YYYY-MM-DD HH:mm') : null,
              csrfToken: this.$cookie.get('csrftoken')
            }
            this.$store.dispatch('createTodo', payload).then(res => {
              console.log(res)
              this.$router.push("/")
            }, error => {
              console.log('createTodo error: ', error)
            })
        }
      },
      clear () {
        this.$v.$reset()
        this.title = ''
        // this.email = ''
        this.content = ''
        this.priority = null
        this.deadineYN = false
        this.deadline = new Date()
      }
    }
  }
</script>
