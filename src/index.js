const dataJson = await fetch("./data.json").then((response) => response.json());

const replaceTemplate = (html, item) => {
  let output = html.replace(/{{%TITLE%}}/g, item.title);
  output = output.replace(/{{%URL%}}/g, item.url);
  output = output.replace(
    /{{%PRICE%}}/g,
    item.price ? `${item.price}Dh` : "No price"
  );
  output = output.replace(/{{%CITY%}}/g, item.city);
  output = output.replace(/{{%CATEGORY%}}/g, item.categoty);
  output = output.replace(/{{%DURATION%}}/g, item.duration);
  output = output.replace(/{{%POSTDATE%}}/g, item.postDate);
  output = output.replace(/{{%IMAGE%}}/g, item.imageUrl);
  if (!item.store) output = output.replace(/{{%STORE%}}/g, "d-none");
  if (!item.isDelivery) output = output.replace(/{{%ISDELIVERY%}}/g, "d-none");
  return output;
};

const renderList = (data) => {
  $.ajax({
    type: "GET",
    url: "./templates/card.html",
    success: (html) => {
      data.forEach((item) => {
        $("#list").append(replaceTemplate(html, item));
      });
    },
  });
  $("#total").text(`${data.length} items`);
};

const sortData = (data, sortBy) => {
  if (sortBy === "default") return data;
  let sortedData = data.sort((a, b) => {
    if (sortBy === "price") {
      return a[sortBy] - b[sortBy];
    } else {
      return a[sortBy].localeCompare(b[sortBy]);
    }
  });
  if (sortBy === "price")
    sortedData = sortedData.filter((item) => item.price !== null);
  return sortedData;
};

const filterIsStore = (data, isStore) => {
  if (isStore !== "on") return data;
  const filteredData = data.filter((item) => item.store === true);
  return filteredData;
};

const filterIsDelivery = (data, isDelivery) => {
  if (isDelivery !== "on") return data;
  const filteredData = data.filter((item) => item.isDelivery === true);
  return filteredData;
};

const searchData = (data, keyword, type) => {
  if (keyword === "") return data;
  const keywordArr = keyword.split(" ");
  const filteredData = data.filter((item) => {
    for (const word of keywordArr) {
      if (!item[type].toLowerCase().includes(word.toLowerCase())) return false;
    }
    return true;
  });
  return filteredData;
};

$("#form").on("submit", function (e) {
  e.preventDefault();
  // let data = dataJson;
  let data = [...dataJson];
  const formData = $(this).serializeArray();
  console.log(formData);
  for (const item of formData) {
    switch (item.name) {
      case "sortBy":
        data = sortData(data, item.value);
        break;
      case "search":
        data = searchData(data, item.value, "title");
        break;
      case "city":
        data = searchData(data, item.value, "city");
        break;
      case "isStore":
        data = filterIsStore(data, item.value);
        break;
      case "isDelivery":
        data = filterIsDelivery(data, item.value);
        break;
      default:
        break;
    }
  }
  $("#list").html("");
  renderList(data);
});

renderList(dataJson);
