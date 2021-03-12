const hsl = require('hsl-to-hex');

const DEFAULTS = {
  SATURATION: 100,
  LIGHTNESS: 50,
  HUE_MAX: 1,
  COEFF: 120,
};

/**
 * Converts percent value (between 0 and 1) to HEX color code (between green and red)
 * 
 * @param {number[]|number} The object [hue, saturation, lightness] or just a hue number from 0 (green) to 1 (red)
 * @throws {Error} Input argument of invalid type 
 * @returns {string} The HEX color code
 */
const percentToHex = function(params) {
    let hue, saturation, lightness;

    if (Array.isArray(params)) {
        hue             = typeof params[0] === 'number' ? params[0] : DEFAULTS.HUE_MAX;
        saturation      = typeof params[1] === 'number' ? params[1] : DEFAULTS.SATURATION;
        lightness       = typeof params[2] === 'number' ? params[2] : DEFAULTS.LIGHTNESS;
    } else if (typeof params == 'number') {
        hue         = params;
        saturation  = DEFAULTS.SATURATION;
        lightness   = DEFAULTS.LIGHTNESS;
    } else {
        throw new Error('Invalid argument');
    }

    if (hue > 1) {
        hue = DEFAULTS.HUE_MAX;
    }

    return hsl(
        ((DEFAULTS.HUE_MAX - hue) * DEFAULTS.COEFF).toString(10),
        saturation,
        lightness,
    ); 
}

module.exports = percentToHex;
