import calculateVat2, {calculateVat,formatPrice,vat_rate} from './utils/format.js';
console.log(formatPrice(calculateVat(18900)));
console.log("calculateVat2: ", formatPrice(calculateVat2(18900)));
console.log("formatPrice: ", formatPrice(1890));
console.log("vat_rate: ", vat_rate);