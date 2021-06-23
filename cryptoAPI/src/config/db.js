const axios = require('axios');

// o IRI da ontologia é local
const prefixes = `
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX noInferences: <http://www.ontotext.com/explicit>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX : <http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#>
`;
const getLink = `http://${process.env.BASE_URL}/repositories/crypto?query=`;

function toJS(response) {
  let list = [];
  const { vars } = response.head;
  list = response.results.bindings.map((e) => {
    const object = {};
    vars.forEach((i) => object[i] = e[i].value);
    return object;
  });
  return list;
}

module.exports.query = async (query) => {
  const encoded = encodeURIComponent(prefixes + query);
  try {
    const result = await axios.get(getLink + encoded);
    return toJS(result.data);
  } catch (err) {
    // eslint-disable-next-line no-undef
    return { error: err };
  }
};
