var x = 0;
var calculate_seed = function() {
    for (;;) {
        var m = new MersenneTwister(x);
        if (((m.genrand_int32() * Math.sqrt(m.random())) & 255) == 198) {
            if (((m.genrand_int32() * Math.sqrt(m.random())) & 255) == 58) {
                if (((m.genrand_int32() * Math.sqrt(m.random())) & 255) == 110) {
                    console.log("Seed " + x + " has passed three tests. This is probably the right seed");
                    break;
                }
            }
        }
        x++;
    }
}

var query2_0 = function() {
    var m = new MersenneTwister(4744);
    // Call three times to get to the random we want
    m.genrand_int32();
    m.random();
    m.genrand_int32();
    m.random();
    m.genrand_int32();
    m.random();
    console.log(String.fromCharCode(((m.genrand_int32() * Math.sqrt(m.random())) & 255) ^ 49));
}

var query2_6 = function() {
    var i = 0;
    for (;;) {
        // -821768299 is h.words.splice(0, 1) when it gets evaluated
        if (String.fromCharCode(i ^ -821768299 & 255) == "s") {
            console.log(String.fromCharCode(i/2));
            break;
        }
        i++;
    }
}

var query2_8 = function() {
    function isInt(n){
        return Number(n) === n && n % 1 === 0;
    }
    var alphabet = "abcdefghijklmnopqrstuvwxyz";
    for(var i=0; i<alphabet.length; i++) {
        var chr = alphabet.charAt(i);
        var num = Math.pow((3111809 - chr.charCodeAt(0)), .25);
        if (isInt(num)) {
            console.log(chr);
            console.log(String.fromCharCode(num ^ 95))
        }
    }
}
