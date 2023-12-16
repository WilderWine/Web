class CProduct{
    constructor(name, description, price){
        this.name = name;
        this.price = price;
        this.description = description;
    }
    get getPrice() {
        return this.price;
    }

    set setPrice(newPrice) {
        this.price = newPrice;
    }
    get getDescription() {
        return this.description;
    }

    set setDescription(newDescription) {
        this.description = newDescription;
    }

    privetstvie(){
        alert('hello, i\'m ' + this.name)
    }

}

class CategorizedCProduct extends CProduct{
    constructor(name, price, description, category){
        super(name, price, description);
        this.category = category;
    }
     get getCategory() {
        return this.category;
    }

    set setDescription(newCategory) {
        this.category = newCategory;
    }

}

function FProduct(name, price, desc){
this.name = name;
this.price = price;
this.desc = desc;
    this.privetstvie() = function() {
        alert('hello, i\'m ' + this.name);
    };
    this.getPrice = function(){return }
}

Product.prototype.setPrice = function (newPrice) {
    this.price = newPrice;
};

function CategorizedFProduct(name,price,desc,category){
    FProduct.call(this,name,price,desc);
    this.category = category;
}

CategorizedFProduct.prototype = Object.create(FProduct.prototype);
CategorizedFProduct.prototype.constructor = CategorizedFProduct;