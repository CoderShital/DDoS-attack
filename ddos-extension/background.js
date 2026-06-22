console.log("Extension Started");
chrome.webNavigation.onCompleted.addListener(
  async (details) => {
    if (details.frameId !== 0) return;
    try {
      const tab = await chrome.tabs.get(details.tabId);
      const response = await fetch(
        "http://127.0.0.1:5000/check",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            url: tab.url
          })
        }
      );
      const result = await response.json();
      console.log(result);
      if (result.block) {
        chrome.tabs.update(
          details.tabId,
          {
            url: chrome.runtime.getURL(
              "blocked.html"
            )
          }
        );
      }
    } catch (err) {
      console.log(err);
    }
    console.log("Page visited:", details.url);
  }
);