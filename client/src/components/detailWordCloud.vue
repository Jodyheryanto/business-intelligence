<template>
    <modal 
      name="example-draggable"
      transition="nice-modal-fade"
      height="auto" 
      :scrollable="true"
      :delay="100"
      :adaptive="true">
    <div class="example-modal-content">
        <h3 style="margin: 15px 20px;">Detail</h3>
        <hr>
        <div class="col-12 col-lg-12 pt-3">
          <div class="profile-widget">
            <div class="profile-widget-header">
              <img alt="image" :src="detail.user_avatar" class="rounded-circle profile-widget-picture">
              <div class="profile-widget-items">
                <div class="profile-widget-item">
                  <div class="profile-widget-item-label">Rating</div>
                  <div class="profile-widget-item-value">{{ detail.rating }} Star</div>
                </div>
                <div class="profile-widget-item">
                  <div class="profile-widget-item-label">Sentiment</div>
                  <div class="profile-widget-item-value">
                    <div v-if="detail.sentiment === 0">
                        <h6 class="badge badge-danger">negative</h6>
                    </div>
                    <div v-if="detail.sentiment === 1">
                        <h6 class="badge badge-success">positive</h6>
                    </div>
                  </div>
                </div>
                <div class="profile-widget-item">
                  <div class="profile-widget-item-label">Keyword</div>
                  <div class="profile-widget-item-value">#{{ word }}</div>
                </div>
              </div>
            </div>
            <div class="profile-widget-description pb-0">
              <div class="profile-widget-name">{{ detail.user_name }} <div class="text-muted d-inline font-weight-normal"><div class="slash"></div> {{ detail.sumber }}</div></div>
              <p>{{ detail.post }}.</p>
            </div>
            <div class="table-wrapper-scroll-y my-custom-scrollbar text-center pt-0 h-100">
              <table class="table table-striped" style="margin-top: 30px; text-align: center">
                <thead>
                  <tr>
                    <th scope="col">Account</th>
                    <th scope="col">Date</th>
                    <th scope="col">Sumber</th>
                    <th scope="col">Post</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><img :src="detail.user_avatar" alt="avatar-2" width="70" height="70" class="rounded-circle" style="margin: 12px 0;"><br>{{ detail.user_name }}</td>
                    <td>{{ detail.tanggal_post }}</td>
                    <td><a :href="detail.link_review" target="_blank">{{ detail.sumber }}</a></td>
                    <td>{{ detail.post }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
  </modal>
</template>
<script>
// import store from '@/store'
export default {
    data() {
        return {
            neww: '',
            neww2: '',
            detail: {
              tanggal_post: null,
              user_name: '',
              user_avatar: '',
              sumber: '',
              link_review: '',
              sentiment: null,
              id: null,
              post: '',
              rating: ''
            },
            word: ''
        }
    },
    mounted() {
      this.$eventBus.$on("datafromwordCloud", (x) => {
        this.neww = x;
        this.detail.user_name = this.neww.user_name
        this.detail.user_avatar = this.neww.user_avatar
        this.detail.link_review = this.neww.link_review
        this.detail.sumber = this.neww.sumber
        this.detail.tanggal_post = this.neww.tanggal_post
        this.detail.post = this.neww.post
        this.detail.rating = this.neww.rating
        this.detail.sentiment = this.neww.sentiment
        this.detail.id = this.neww.id
      });
      this.$eventBus.$on("datafromwordCloud2", (x) => {
        this.neww2 = x;
        this.word = this.neww2[0]
      });
      //this.items.push({isActive: true, date: data.book.critic_reviews[i].review_date, source: data.book.critic_reviews[i].source, rating: data.book.critic_reviews[i].star_rating, sentiment: data.book.critic_reviews[i].pos_or_neg, post: data.book.critic_reviews[i].snippet, link_review: data.book.critic_reviews[i].review_link,account: { username: this.users[i].name, image: this.users[i].avatar }})
      // this.items.push({id: this.detail.id, account: { username: this.detail.user_name, user_avatar: this.detail.user_avatar }, post: this.detail.post, tanggal_post: this.detail.tanggal_post, sumber: this.detail.sumber, link_review: this.detail.link_review, rating: this.detail.rating, sentiment: this.detail.sentiment})
      // console.log(this.items[0])
    },
    methods: {
    }
}
</script>

<style scope>
  li{
    padding-bottom: 10px;
  }
  .borderless td, .borderless th {
      border: none;
  }
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding-right: 30px;
    padding-top: 10px;
  }

  .btn-close {
    border: none;
    font-size: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-blue {
    color: white;
    font-weight: bold;
    font-size: 13px;
    background: #0044ff;
    border: 1px solid #4AAE9B;
    border-radius: 5px;
    padding: 5px;
  }

  .btn-green {
    color: white;
    font-weight: bold;
    font-size: 13px;
    background: #22ff00;
    border: 1px solid #4AAE9B;
    border-radius: 5px;
    padding: 5px;
  }

  .btn-red {
    margin-left: 2px;
    color: white;
    font-weight: bold;
    font-size: 13px;
    background: red;
    border-radius: 5px;
    padding: 5px;
  }
</style>