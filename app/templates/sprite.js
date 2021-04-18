(function() {
    function Sprite(url, pos, size, speed, frames, dir, once) {
        this.pos = pos;
        this.size = size;
        this.speed = typeof speed === 'number' ? speed : 0;
        this.frames = frames;
        this._index = 0;
        this.url = url;
        this.dir = dir || 'horizontal';
        this.once = once;
    };

    Sprite.prototype = {
        update: function() {
            this._index += 1;
        },

        render: function(board_ctx) {
            var frame;
            var max = this.frames.length;
            //restart if get to end of sprite file
            if (this._index == max) {
                frame = this.frames[0];
                this._index = 0;
            }
            frame = this.frames[this._index];

            if(this.once) {
                this.done = true;
                return;
            }


            var x = this.pos[0];
            var y = this.pos[1];


            board_ctx.drawImage(resources.get(this.url),
                          x, y,
                          this.size[0], this.size[1],
                          0, 0,
                          this.size[0], this.size[1]);
        }
    };

    window.Sprite = Sprite;
})();
