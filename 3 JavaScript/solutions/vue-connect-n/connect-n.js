// connect-n.js
Vue.component('cell', {
  props: ['position'],
  template: `<div @click='$emit("move")'>
      <div v-if='position' v-bind:class='position.token'> </div>
    </div>`
})


const app = new Vue({
  el: '#app',
  data: {
    n: 5,
    size: 8,
    round: 0,
    players: [
      {name: 'Player 1', token: 'white'},
      {name: 'Player 2', token: 'black'},
    ],
    winner: null,
    message: 'Player 1\'s turn',
    score: {'Player 1': 0, 'Player 2': 0},
    board: [...Array(8)].map(row => Array(8).fill(null)),
  },
  methods: {
    addToken(i, j) {
      // check if position is taken
      if (!this.winner) {
        if (this.board[i][j]) {
          this.message = 'Invalid Move'
        } else {
          // place current player on board
          this.board[i][j] = this.player
          // see if it's a winning move
          const winner = this.calcWinner(i, j)
          this.winner = winner
          if (winner) {
            this.message = `${winner.name} wins!`
            this.score[winner.name]++
            return
          }
          // increment round
          this.round++
          this.message = `${this.player.name}'s turn`        
        }
      }
    },
    calcWinner(i, j) {
      const deltas = {
        left: [0, -1], right: [0, 1],
        up: [-1, 0], down: [1, 0],
        ldiagup: [-1, -1], ldiagdown: [1, 1], 
        rdiagup: [-1, 1], rdiagdown: [1, -1], 
      }
      const directions = {
        left: 'right',
        up: 'down',
        ldiagup: 'ldiagdown',
        rdiagup: 'rdiagdown'
      }

      for (let direction in directions) {
        const n = parseInt(this.n)
        // search for matches in this direction
        let matches = this._matches([i, j], deltas[direction])
        if (matches === n) return this.player
        // search for matches in opposite direction
        const opposite = directions[direction]
        matches = this._matches([i, j], deltas[opposite], matches) 
        if (matches === n) 
          return this.player
      }
      return null
    },
    _matches(position, direction, matches=1) {
      const delta = [position[0]+direction[0], position[1]+direction[1]]
      const [di, dj] = delta
      // base case: matches === n
      if (matches === parseInt(this.n)) return matches
      // base case: check if delta is within the bounds of the board
      if (di < 0 || di >= this.size || dj < 0 || dj >= this.size) return matches
      // base case: check if this position does not have the current player 
      if (this.board[di][dj] !== this.player) return matches
      // recursive case: keep checking for matches
      return this._matches(delta, direction, matches+1)
    },
    reset() {
      // clear board to size x size board
      const size = parseInt(this.size)
      this.board = [...Array(size)].map(row => Array(size).fill(null))
      this.winner = null
    }
  },
  computed: {
    player() {
      return this.players[this.round%2]
    }
  }
})