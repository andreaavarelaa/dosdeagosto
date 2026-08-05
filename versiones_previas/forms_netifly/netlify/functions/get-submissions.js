// Netlify Function: devuelve las respuestas de un formulario de Netlify Forms en JSON.
// Requiere dos variables de entorno configuradas en Netlify (Site settings > Environment variables):
//   NETLIFY_API_TOKEN  -> Personal Access Token (User settings > Applications > New access token)
//   NETLIFY_SITE_ID    -> API ID del sitio (Site settings > General > Site details)

exports.handler = async function (event) {
  const TOKEN = process.env.NETLIFY_API_TOKEN;
  const SITE_ID = process.env.NETLIFY_SITE_ID;
  const formName = event.queryStringParameters && event.queryStringParameters.form;

  if (!TOKEN || !SITE_ID) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Faltan las variables de entorno NETLIFY_API_TOKEN o NETLIFY_SITE_ID en Netlify.' })
    };
  }

  if (!formName) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Falta el parámetro ?form=' }) };
  }

  try {
    // 1. Buscar el ID interno del formulario por su "name"
    const formsRes = await fetch(`https://api.netlify.com/api/v1/sites/${SITE_ID}/forms`, {
      headers: { Authorization: `Bearer ${TOKEN}` }
    });
    if (!formsRes.ok) throw new Error('No se pudo listar los formularios (HTTP ' + formsRes.status + ')');
    const forms = await formsRes.json();
    const form = forms.find((f) => f.name === formName);

    if (!form) {
      // El formulario existe en el HTML pero Netlify aún no lo ha indexado
      // (esto pasa hasta que se hace al menos un deploy con el form ya en el HTML).
      return { statusCode: 200, headers: { 'Content-Type': 'application/json' }, body: JSON.stringify([]) };
    }

    // 2. Pedir las respuestas de ese formulario
    const subsRes = await fetch(`https://api.netlify.com/api/v1/forms/${form.id}/submissions`, {
      headers: { Authorization: `Bearer ${TOKEN}` }
    });
    if (!subsRes.ok) throw new Error('No se pudieron leer las respuestas (HTTP ' + subsRes.status + ')');
    const submissions = await subsRes.json();

    // Más recientes primero
    const data = submissions
      .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      .map((s) => s.data);

    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    };
  } catch (err) {
    return { statusCode: 500, body: JSON.stringify({ error: err.message }) };
  }
};
