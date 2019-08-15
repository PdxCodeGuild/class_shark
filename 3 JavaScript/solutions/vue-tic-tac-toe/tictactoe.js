// tictactoe.js vue implementation
Vue.component('cell', {
  props: ['position', 'i', 'addToken'],
  template:  `<div @click="addToken(i)">
                <span v-if='position'>{{position.token}}</span>
              </div>`
})


const app = new Vue({
  el: '#app',
  data: {
    message: 'Player 1\'s turn',
    players: [
      {name: 'Player 1', token: 'O', class:'one'},
      {name: 'Player 2', token: 'X', class:'two'}
    ],
    round: 1,
    board: Array.from(Array(9)), // empty array of length 9
  },
  methods: {
    addToken(idx) {
      this.message = `${this.player.name}'s turn`
      if (this.board[idx]) { 
      // position taken
        this.message = 'Invalid move'
      } else { 
      // move player to position and increment round
        this.board[idx] = this.player
        this.round++
        return this.gameOver()
      }
    },
    calcWinner() {
      for (let i=0; i<3; i++) {
        // horizontal wins
        const hcell = this.board[3*i]
        if (hcell && (this.board.slice(3*i, 3*i+3).filter(elem => elem === hcell).length === 3)) {
          console.log('horizontal', 3*i, 3*i+3, (this.board.slice(3*i, 3*i+3)))
          return hcell
        }
        // vertical wins
        const vcell = this.board[i]
        if (vcell && [this.board[i], this.board[i+3], this.board[i+6]].filter(elem => elem === vcell).length === 3) {
          console.log('vertical', i, i+3, i+6, ([this.board[i], this.board[i+3], this.board[i+6]]))
          return vcell
        }
      }
      // diagonal wins
      const cell = this.board[4] // center
      if (cell && this.board[0] === cell && cell === this.board[8]) return cell
      if (cell && this.board[2] === cell && cell === this.board[6]) return cell

      return null
    },
    boardFull() {
      for (let i=0; i<this.board.length; i++) {
        if (!this.board[i]) return false
      }
      return true
    },
    gameOver() {
      const winner = this.calcWinner()
      const message = (winner ? winner.name : false) || (this.boardFull() ? 'tie' : false)
      if (message) this.message = 'Winner: ' + message
      return message
    },
    reset() {
      this.board = Array.from(Array(9))
    }
  },
  computed: {
    player() {
      return this.players[this.round%2]
    },
  }
})