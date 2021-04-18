
function main() {
    render();
    requestAnimFrame(main);
};


function init() {
    main();
}

function update() {
    //gameTime += dt;

    //handleInput(dt);
    updateEntities();
};

function updateEntities() {
    // Update the player sprite animation
    player.sprite.update();
}
    // Draw everything
    function render() {
        renderEntity(background);
        renderEntities(playerImage);
        renderEntities(boulderImage);
    };
    
    function renderEntities(list) {
        for(var i=0; i<list.length; i++) {
            renderEntity(list[i]);
        }    
    }
    
    function renderEntity(entity) {
        board_ctx.save();
        board_ctx.translate(entity.pos[0], entity.pos[1]);
        entity.sprite.render(board_ctx);
        board_ctx.restore();
    }
