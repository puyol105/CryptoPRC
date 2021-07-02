<template>
  <div>

    <v-card-text>
      <h2 class="text-h6 mb-2">
          Algorithms:
      </h2>
      <v-chip-group
          active-class="primary--text"
          column
          
        >
          <v-chip
            v-for="(item, index) in algorithm"
            :key="index"
            :href="`/tag/algorithm/${item.link}`"
          >
            {{ item.name }} 
          </v-chip>
      </v-chip-group>
    </v-card-text>
    
   <v-card-text>
      <h2 class="text-h6 mb-2">
          Plataform:
      </h2>
      <v-chip-group
          active-class="primary--text"
          column
          
        >
          <v-chip
            v-for="(item, index) in plataform"
            :key="index"
            :href="`/tag/plataform/${item.link}`"
          >
            {{ item.name }} 
          </v-chip>
      </v-chip-group>
    </v-card-text>

   <v-card-text>
      <h2 class="text-h6 mb-2">
          Industry:
      </h2>
      <v-chip-group
          active-class="primary--text"
          column
          
        >
          <v-chip
            v-for="(item, index) in industry"
            :key="index"
            :href="`/tag/industry/${item.link}`"
          >
            {{ item.name }} 
          </v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-text>
      <h2 class="text-h6 mb-2">
          Category:
      </h2>
      <v-chip-group
          active-class="primary--text"
          column
          
        >
          <v-chip
            v-for="(item, index) in category"
            :key="index"
            :href="`/tag/category/${item.link}`"
          >
            {{ item.name }} 
          </v-chip>
      </v-chip-group>
    </v-card-text>


  </div>
</template>


<script>
import { mapGetters } from "vuex";
export default {
  name: "Tags",
  data: () => {
    return {
        category: [],
        algorithm: [],
        industry: [],
        plataform: [],
        page: 1,
        totalItems: 0,
        numberOfPages: 0,
        loading: true,
        options: {

        },
        headers1: [
            
      ],
      items1: [],
    }
  },

  created() {
    console.log('created')
    this.getTags('Industry')
    this.getTags('Plataform')
    this.getTags('Category')
    this.getTags('Algorithm')
  },    

  methods: {
      getTags(tag){
        this.$request("get", `tags/${tag}`)
          .then((data) => {
            console.log('get tags data-total', data)
            switch(tag) {
              case 'Industry' :
                this.industry = data.data
                break
              case 'Plataform' :
                this.plataform = data.data
                break
              case 'Category' :
                this.category = data.data
                break
              case 'Algorithm' :
                this.algorithm = data.data
                break
              default:
                console.log('Tag não existe')
            }
            
          })
          .catch((e) => console.log(e));
        },
  
    },


  computed: {
    ...mapGetters(["carts"]),
  },
};
</script>
