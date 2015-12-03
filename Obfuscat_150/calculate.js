var x = 0;
var seed = function() {
    for (;;) {
        var m = new MersenneTwister(x);
        if (((m.genrand_int32() * Math.sqrt(m.random())) & 255) == 198) {
            if (((m.genrand_int32() * Math.sqrt(m.random())) & 255) == 58) {
                if (((m.genrand_int32() * Math.sqrt(m.random())) & 255) == 110) {
                    alert("Seed " + x + " has passed three tests. This is probably the right seed");
                    break;
                }
            }
        }
        x++;
    }
}

var idk = function() {
    var m = new MersenneTwister(4744);
    // Call three times to get to the random we want
    m.genrand_int32();
    m.random();
    m.genrand_int32();
    m.random();
    m.genrand_int32();
    m.random();
    alert((m.genrand_int32() * Math.sqrt(m.random())) & 255);
}

var wat = function() {
    var i = 0;
    for (;;) {
        if (String.fromCharCode(i ^ -821768299 & 255) == "s") {
            console.log(i);
            break;
        }
        i++;
    }
}
