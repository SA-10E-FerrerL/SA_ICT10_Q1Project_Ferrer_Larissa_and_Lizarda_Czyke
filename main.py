from pyscript import display, document
#Basic thingy, the calm before the storm
def SKU_generator(e):
    document.getElementById('sku_output').innerHTML = ""

    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    quantity = document.getElementById("quantity").value

    #Stops users from using select product or category in a SKU
    if category == "SAC" or product_name == "SAP":
        alert("Please select a category and product.")
        return
    
    sku = category[:3].upper() + product_name[:3].upper() + str(quantity)[:2]

    display("Your SKU is: " +sku, target="sku_output")

#Literally the worst eyesore I've ever seen in my coding
def create_order(e):

    order_summary = document.getElementById("order_summary")
    order_summary.innerHTML = ""

    #Checks to see which items you chose
    product1check = document.getElementById("item1")
    product2check = document.getElementById("item2")
    product3check = document.getElementById("item3")
    product4check = document.getElementById("item4")
    product5check = document.getElementById("item5")
    product6check = document.getElementById("item6")
    product7check = document.getElementById("item7")
    product8check = document.getElementById("item8")
    product9check = document.getElementById("item9")
    product10check = document.getElementById("item10")
    product11check = document.getElementById("item11")
    product12check = document.getElementById("item12")
    product13check = document.getElementById("item13")
    product14check = document.getElementById("item14")
    product15check = document.getElementById("item15")

    #Gets the numerical price of each item
    numberprice1= document.getElementById("item1").value
    numberprice2= document.getElementById("item2").value
    numberprice3= document.getElementById("item3").value
    numberprice4= document.getElementById("item4").value
    numberprice5= document.getElementById("item5").value
    numberprice6= document.getElementById("item6").value
    numberprice7= document.getElementById("item7").value
    numberprice8= document.getElementById("item8").value
    numberprice9= document.getElementById("item9").value
    numberprice10= document.getElementById("item10").value
    numberprice11= document.getElementById("item11").value
    numberprice12= document.getElementById("item12").value
    numberprice13= document.getElementById("item13").value
    numberprice14= document.getElementById("item14").value
    numberprice15= document.getElementById("item15").value

    #Labels for each item
    product1text = document.getElementById("item1-label").textContent
    product2text = document.getElementById("item2-label").textContent
    product3text = document.getElementById("item3-label").textContent
    product4text = document.getElementById("item4-label").textContent
    product5text = document.getElementById("item5-label").textContent
    product6text = document.getElementById("item6-label").textContent
    product7text = document.getElementById("item7-label").textContent
    product8text = document.getElementById("item8-label").textContent
    product9text = document.getElementById("item9-label").textContent
    product10text = document.getElementById("item10-label").textContent
    product11text = document.getElementById("item11-label").textContent
    product12text = document.getElementById("item12-label").textContent
    product13text = document.getElementById("item13-label").textContent
    product14text = document.getElementById("item14-label").textContent
    product15text = document.getElementById("item15-label").textContent

    #The price but in text form to be put next to the labels
    textprice1 = document.getElementById("price1").textContent
    textprice2 = document.getElementById("price2").textContent
    textprice3 = document.getElementById("price3").textContent
    textprice4 = document.getElementById("price4").textContent
    textprice5 = document.getElementById("price5").textContent
    textprice6 = document.getElementById("price6").textContent
    textprice7 = document.getElementById("price7").textContent
    textprice8 = document.getElementById("price8").textContent
    textprice9 = document.getElementById("price9").textContent
    textprice10 = document.getElementById("price10").textContent
    textprice11 = document.getElementById("price11").textContent
    textprice12 = document.getElementById("price12").textContent
    textprice13 = document.getElementById("price13").textContent
    textprice14 = document.getElementById("price14").textContent
    textprice15 = document.getElementById("price15").textContent

    #Lists all the items and prices, no math
    order = ((product1text + ": " + textprice1 + "\n")*product1check.checked)+((product2text + ": " + textprice2 + "\n")*product2check.checked)+((product3text + ": " + textprice3 + "\n")*product3check.checked)+((product4text + ": " + textprice4 + "\n")*product4check.checked)+((product5text + ": " + textprice5 + "\n")*product5check.checked)+((product6text + ": " + textprice6 + "\n")*product6check.checked)+((product7text + ": " + textprice7 + "\n")*product7check.checked)+((product8text + ": " + textprice8 + "\n")*product8check.checked)+((product9text + ": " + textprice9 + "\n")*product9check.checked)+((product10text + ": " + textprice10 + "\n")*product10check.checked)+((product11text + ": " + textprice11 + "\n")*product11check.checked)+((product12text + ": " + textprice12 + "\n")*product12check.checked)+((product13text + ": " + textprice13 + "\n")*product13check.checked)+((product14text + ": " + textprice14 + "\n")*product14check.checked)+((product15text + ": " + textprice15 + "\n")*product15check.checked)

    #Calculates the total cost, all the math is here
    total_cost=(float(numberprice1)*product1check.checked)+(float(numberprice2)*product2check.checked)+(float(numberprice3)*product3check.checked)+(float(numberprice4)*product4check.checked)+(float(numberprice5)*product5check.checked)+(float(numberprice6)*product6check.checked)+(float(numberprice7)*product7check.checked)+(float(numberprice8)*product8check.checked)+(float(numberprice9)*product9check.checked)+(float(numberprice10)*product10check.checked)+(float(numberprice11)*product11check.checked)+(float(numberprice12)*product12check.checked)+(float(numberprice13)*product13check.checked)+(float(numberprice14)*product14check.checked)+(float(numberprice15)*product15check.checked)
    taxrate=.12
    tax=total_cost*taxrate
    total_cost=total_cost+tax

    #Here solely to allow line breaks after each item
    document.getElementById("order_summary").style.whiteSpace = "pre-line"

    display("Order Summary: \n" + str(order) + "VAT: €" + str(tax) + "\nTotal Cost: €" + str(total_cost) + "\nYour order has been processed, please shop with us again! :>", target="order_summary")
