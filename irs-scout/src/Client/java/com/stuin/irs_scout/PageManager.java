package com.stuin.irs_scout;

import android.content.Context;
import android.view.Gravity;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;
import com.stuin.irs_scout.Views.Page;

import java.util.ArrayList;
import java.util.List;

class PageManager extends LinearLayout {
    private List<Page> pages = new ArrayList<>();
    private Request request;
    String position;
    private int current = -1;

    PageManager(Context context, Request request, String position) {
        //Start Layout
        super(context);
        this.request = request;
        this.position = position;

        //Setup centering
        LayoutParams lp = new LayoutParams(LayoutParams.MATCH_PARENT,LayoutParams.MATCH_PARENT);
        setLayoutParams(lp);
        setGravity(Gravity.CENTER);

        //Generate Pages
        pages = new LabelMaker().pages(request,this);

        //Set default page
        current = 0;
        setPage();
        if(pages.size() > 1)findViewById(R.id.Next);
    }

    Page makePage(String name) {
        current++;
        Page page = new Page(getContext(), name);
        page.setVisibility(GONE);
        addView(page);
        return page;
    }

    void nextPage(View view) {
        //Show next page
        pages.get(current).setVisibility(GONE);
        current++;

        //Set shown buttons
        findViewById(R.id.Previous).setVisibility(VISIBLE);
        if(current + 1 == pages.size()) view.setVisibility(GONE);

        setPage();
    }

    void lastPage(View view) {
        //Show next page
        pages.get(current).setVisibility(GONE);
        current--;

        //Set shown buttons
        findViewById(R.id.Next).setVisibility(VISIBLE);
        if(current == 0) view.setVisibility(GONE);

        setPage();
    }

    private void setPage() {
        pages.get(current).setVisibility(VISIBLE);

        TextView textView = (TextView) findViewById(R.id.PageStatus);
        //textView.setText(pages.get(current).name);

        //Notify server
        request.post("Tablet/" + position, "Page" + current);
    }
}
