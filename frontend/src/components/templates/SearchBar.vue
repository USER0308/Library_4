<template>
  <el-input placeholder="请输入搜索内容" v-model="searchContent" class="input-with-select">
    <el-select v-model="searchType" slot="prepend" id="search-type" placeholder="书名">
      <el-option label="书名" value="bookName"></el-option>
      <el-option label="出版社" value="bookPublisher"></el-option>
      <el-option label="作者" value="bookAuthor"></el-option>
      <el-option label="ISBN" value="bookISBN"></el-option>
    </el-select>
    <el-button slot="append" icon="el-icon-search" @click="deal_query_book"></el-button>
  </el-input>
</template>
<script>
  export default {
    data () {
      return {
        searchType: 'bookName',
        searchContent: ''
      }
    },
    methods: {
      deal_query_book () {
        console.log('searching === start ===')
        console.log('searchType is ' + this.searchType)
        console.log('searchContent is ' + this.searchContent)
        console.log('searching === end ===')
        let win = this
        // query book
        this.$http.get('/api/query_book/', {
          'params': {
            query_type: this.searchType,
            query_keyword: this.searchContent
          }
        }).then((res) => {
          let bookList = res.data.book_list
          console.log('query book from server, get result: === start ===')
          console.log(bookList)
          win.$emit('getQueryResult', bookList)
          console.log('query book from server, get result: === end ===')
        }, (err) => {
          console.log('query book from server, get error: === start ===')
          console.log(err)
          console.log('query book from server, get error: === end ===')
        })
      }
    }
  }
</script>

<style>
  #search-type {
    width: 90px;
  }
</style>
